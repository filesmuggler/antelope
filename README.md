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


### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

