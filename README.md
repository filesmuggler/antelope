# Antelope

Project contains desktop and microcontroller applications. Desktop (named Addax) is written in Python and provides user interface for choosing right parameters for the PWM signal generated on the microcontroller by the embedded application (named Hirola), written in C. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

#### Desktop Application

The desktop app is suited to run on Windows, Linux and Mac machines, since it's written in Python. All you need is install Python interpreter from [Python Official Website](https://www.python.org/). Additionally you will need some packages to run the program smoothly:

- pyserial

```
pip -m install pyserial
```

Make sure to update pip tool.

```
python -m pip install --upgrade pip
```

#### Microcontroller Application

The embedded application is suited for the Analog Devices [ADuC831 microcontroller](https://www.analog.com/media/en/technical-documentation/data-sheets/aduc831.pdf) and is using its capabilities to receive data from the desktop app, interpret them and conttrol output PWM signal. To open, compile and flash the code you should obtain the copy of [Keil Arm uVision IDE](http://www2.keil.com/mdk5/uvision/). It's free of charge and lets you debug programs up to 2kb of code volume.

All code is in (antelope/uController_App/Hirola)

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [MS Visual Studio 2017](https://visualstudio.microsoft.com/) - Desktop app development
* [Keil uVision 5](http://www2.keil.com/mdk5/uvision/) - Microcontroller app development

## Authors

* **Krzysztof Stężała** - *Initial work* - [Filesmuggler](https://github.com/filesmuggler)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Project was designed as an assignment for Microprocessor Systems Laboratory Classes at Poznan University of Technology

