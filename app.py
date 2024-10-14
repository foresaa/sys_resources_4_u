from flask import Flask, render_template, jsonify
import psutil
import GPUtil
import platform

app = Flask(__name__)

# Helper functions to format the system information
def format_size(size_in_bytes):
    return f"{size_in_bytes / (1024 ** 3):.2f}"  # Convert bytes to GB with 2 decimal places

def format_percentage(value):
    return f"{value:.2f}"

def get_system_info():
    uname = platform.uname()
    return [
        ["System", uname.system],
        ["Node Name", uname.node],
        ["Release", uname.release],
        ["Version", uname.version],
        ["Machine", uname.machine],
        ["Processor", uname.processor]
    ]

def get_cpu_info():
    cpu_info = [
        ["Physical Cores", psutil.cpu_count(logical=False)],
        ["Total Cores", psutil.cpu_count(logical=True)],
        ["Max Frequency (GHz)", format_percentage(psutil.cpu_freq().max)],
        ["Min Frequency (GHz)", format_percentage(psutil.cpu_freq().min)],
        ["Current Frequency (GHz)", format_percentage(psutil.cpu_freq().current)],
        ["Total CPU Usage (%)", format_percentage(psutil.cpu_percent())]
    ]
    return cpu_info

def get_memory_info():
    svmem = psutil.virtual_memory()
    memory_info = [
        ["Total Memory (GB)", format_size(svmem.total)],
        ["Available Memory (GB)", format_size(svmem.available)],
        ["Used Memory (GB)", format_size(svmem.used)],
        ["Percentage Used (%)", format_percentage(svmem.percent)]
    ]
    return memory_info

def get_disk_info():
    partitions = psutil.disk_partitions()
    disk_info = [["Device", "Total Size (GB)", "Used (GB)", "Free (GB)", "Usage (%)"]]
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_info.append([
            partition.device,
            format_size(usage.total),
            format_size(usage.used),
            format_size(usage.free),
            format_percentage(usage.percent)
        ])
    return disk_info

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    gpu_info = [["GPU Name", "Total Memory (GB)", "Free Memory (GB)", "Used Memory (GB)", "GPU Load (%)", "Temperature (C)"]]
    for gpu in gpus:
        gpu_info.append([
            gpu.name,
            format_size(gpu.memoryTotal * 1024 ** 2),  # Convert MB to GB
            format_size(gpu.memoryFree * 1024 ** 2),
            format_size(gpu.memoryUsed * 1024 ** 2),
            format_percentage(gpu.load * 100),
            gpu.temperature
        ])
    return gpu_info if len(gpus) > 0 else [["No GPU found", "", "", "", "", ""]]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_resources', methods=['GET'])
def get_resources():
    system_info = get_system_info()
    cpu_info = get_cpu_info()
    memory_info = get_memory_info()
    disk_info = get_disk_info()
    gpu_info = get_gpu_info()
    
    return jsonify({
        'system_info': system_info,
        'cpu_info': cpu_info,
        'memory_info': memory_info,
        'disk_info': disk_info,
        'gpu_info': gpu_info
    })

if __name__ == "__main__":
    app.run(debug=True)
