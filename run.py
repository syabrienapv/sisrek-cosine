from main import app

if __name__ == "__main__":
    app.run(debug=True)

from main import prediksi

prediksi.read_dataset()
prediksi.read_sparse()