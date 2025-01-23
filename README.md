# Radxa-X4 RP2040 Notua PWM-FanControl 
PWM-Control for Fans on the Radxa-x4 using the built in rp2040 microcontroller

# Equipment needed
* soldering equiment
* copper wire
* dupont-set

* crimping pliers
* wire stripper
* Noctua NF-A4x20-PWM


# Create the Cable
The noctua-fan comes with a handy little adapter.
Image below.
<br><img width="500" alt="Adapter" src="https://github.com/user-attachments/assets/e469452d-e1f4-4b3f-a87a-7e138a45853e" /><br>
This adapter has two empty slots for dupont-pins to make this fan work with pwm. 
For the mod u just need to populate the outer spot of the adapter and crimp it with dupont-male on one side and female on the other. 
Also extend the red and black wire and also crimp it with dupont female.
After u are finished you will have something that looks like this. (image below)
<br><img width="500" alt="Modded Adapter" src="https://github.com/user-attachments/assets/046d1207-43c1-44fe-be01-aa25fdf17ff6" /><br>

# Pinout
[Radxa-x4 Pinout in Docs](https://docs.radxa.com/en/x/x4/software/gpio)
![GPIO](https://github.com/user-attachments/assets/888ec105-db01-4599-957c-cd892e216e99)
Connect ground (black) to one of the black terminals on the radxa-x4 (Best is pin 6), connect red to one od the two red terminals (best is pin 4) and last connect the pwm-wire in color blue preferably to pin 8.

# Finished Hardware-setup
<br><img width="500" alt="Modded Adapter" src="https://github.com/user-attachments/assets/5c1a86ae-3d6a-4bd1-8985-794f90a8e23f"/><br>
<br><img width="500" alt="Modded Adapter" src="https://github.com/user-attachments/assets/24042dc0-6a00-4761-94f7-7c1748f8b39c"/><br>

# Flash MicroPython onto the RP2040 on the Radxa-x4
Download the project to the radxa-x4 via git or wget or curl.
```sh
git clone https://github.com/arag0re/radxa_x4-rp2040-notua-pwm
```
Download Micropython for the RP2040 using wget from [micropython.org](https://micropython.org/download/RPI_PICO/").
```sh
wget https://micropython.org/resources/firmware/RPI_PICO-20241129-v1.24.1.uf2
```
U will need `sudo apt install gpiod` for the script to work on Ubuntu! idk about the other distros.
Then create a new bash script using your favorite texteditor called `usb.sh` with the following content or use the one included in this repository:
```bash
#! /bin/bash

sudo gpioset gpiochip0 17=1
sudo gpioset gpiochip0 7=1

sleep 1

sudo gpioset gpiochip0 17=0
sudo gpioset gpiochip0 7=0
```
Make it executable using chmod: 
```sh
sudo chmod a+x ./usb.sh
```
Now execute it to bring the rp2040 into bootloader mode:
```sh
./usb.sh
```
Now you should see a new device listed under `/dev/` in my case it was `sda`.
You can check and find it with `lsblk`. 
If u found it mount it under a freshly created folder:
```sh
mkdir /mnt/pico && sudo mount /dev/sda1 /mnt/pico
ls /mnt/pico
>INDEX.HTM  INFO_UF2.TXT
```
Copy the uf2 to this device and it should unmount and now run micropython.
```sh
cp ~/Downloads/RPI_PICO-20241129-v1.24.1.uf2 /mnt/pico
```
Its helpful to use vscode-ssh-remote-dev addons to flash the micropython code to the rp2040 using the [micropico-addon](https://marketplace.visualstudio.com/items?itemName=paulober.pico-w-go)
