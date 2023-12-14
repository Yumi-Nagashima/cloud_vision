import subprocess


def run_command():
    command = ["python", "SwinIR-main\main_test_swinir.py",
               "--task", "real_sr",
               "--model_path", "D:\\number_plate\\ocr\\cloud_vision\\SwinIR-main\\003_realSR_BSRGAN_DFO_s64w8_SwinIR-M_x4_GAN.pth",
               "--folder_lq", "D:\\number_plate\\ocr\\cloud_vision\\sample\\image09_0.jpg",
               "--scale", "2",
               "--large_model"]
    subprocess.run(command)

if __name__ == "__main__":
    run_command()