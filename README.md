# 🚗 License Plate Detection with YOLOv9

This project is a **real-time Iranian license plate detection system** powered by **YOLOv9**.  
It can detect and localize license plates from live webcam feeds or static images.

---

## 📂 Project Structure

```
IR-LPR/
│   main.py            # Run the webcam inference script
│   requirements.txt   # Required Python dependencies
│   training.ipynb     # Jupyter notebook for training the YOLOv9 model
│
└───Data
    │   model.pt       # Trained YOLOv9 model weights
```

---

## ⚡ Installation

1. Clone this repository:
```bash
git clone https://github.com/AmirSalajegheh/IR-LPR.git
cd IR-LPR
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Make sure **PyTorch** is installed with CUDA support if you plan to use a GPU.

---

## 🚀 Usage

### Run with Webcam:
```bash
python main.py
```

### Train the Model:
Open `training.ipynb` in Jupyter Notebook or Google Colab and follow the steps to train on your dataset.

---

## 📊 Example Results

After running `main.py`, results will be saved in the `Data/` folder. Example:

- `Data/output.jpg` shows detected license plates.

---

## 🛠️ Tech Stack

- [PyTorch](https://pytorch.org/)
- [Ultralytics YOLOv9](https://github.com/ultralytics/ultralytics)
- [OpenCV](https://opencv.org/)

---

## 👨‍💻 Author

Developed by **Amir Salajegheh** 🚀
