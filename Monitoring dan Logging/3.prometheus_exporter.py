import http.server
import random
import time
try:
    from prometheus_client import start_http_server, Gauge  # type: ignore
except ImportError:
    print("Error: prometheus_client module is not installed.")
    print("Please install it using: pip install prometheus-client")
    exit(1)

# 1. Definisikan metrik yang akan dimonitor
# Menggunakan Gauge karena nilai akurasi dan latensi bisa naik turun
MODEL_ACCURACY = Gauge('annisa_model_accuracy', 'Akurasi dari model Titanic')
MODEL_LATENCY = Gauge('annisa_model_latency_seconds', 'Waktu respon model dalam detik')
PREDICTION_COUNT = Gauge('annisa_prediction_total', 'Total prediksi yang dilakukan')

def process_request():
    """Simulasi pemrosesan metrik model"""
    # Simulasi akurasi antara 0.80 - 0.95
    MODEL_ACCURACY.set(random.uniform(0.80, 0.95))
    
    # Simulasi latensi antara 0.01 - 0.05 detik
    MODEL_LATENCY.set(random.uniform(0.01, 0.05))
    
    # Tambah hitungan prediksi
    PREDICTION_COUNT.inc()

if __name__ == '__main__':
    # 2. Start server exporter di port 8000
    # Port ini harus sesuai dengan yang ada di file prometheus.yml kamu
    start_http_server(8000)
    print("Prometheus Exporter jalan di http://localhost:8000")
    print("Tekan Ctrl+C untuk berhenti")

    # 3. Loop untuk terus memperbarui data secara otomatis
    while True:
        process_request()
        time.sleep(5)  # Update data setiap 5 detik