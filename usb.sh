#! /bin/bash

sudo gpioset gpiochip0 17=1
sudo gpioset gpiochip0 7=1

sleep 1

sudo gpioset gpiochip0 17=0
sudo gpioset gpiochip0 7=0