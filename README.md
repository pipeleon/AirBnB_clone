<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png" style="height:50%;width:50%" />

# Overview

The beginning of a multi-part Airbnb clone project which are creates a copy of [Airbnb](https://www.airbnb.com/). We have created a console that allows for the creation and manipulation of objects in a user-friendly interface.
## Getting Started:
The first step to running the console requires a cloning of the repository which can be done in the following way:
`$ git clone https://github.com/pipeleon/AirBnB_clone.git`
Once cloned, to run the program type:
`$ ./console`
## Features
As stated above, this particular piece of the AirBnB clone is a console, i.e. a command intepreter that allows for the developer to be able to contact and control various objects on a high level. See below for more details.
### Command Interpreter
#### Description
Modifies the application's functionality from the command line, i.e.:
+ Creates a new object.
+ Retrieves an object.
+ Provides data on objects such as their id numbers and details specific to the object, e.g. Place object can have a certain number of rooms which the console can display
+ Update and/or add attributes to an object.
+ Destroys object.
#### Usage
To launch the console application in interactive mode run the following:
```./console.py ```
If non-interactive mode is desired run:
```echo "command" | ./console.py ```
#### Commands
Commands | Description | Usage
-------- | ----------- |-------- |
**help** or **?**| Displays the documented commands. | **help**
**quit**     | Exits the program. | **quit**
**EOF**      | Also exits the program. Used when files are passed into the program. | N/A
**create**  | Creates a new instance of a specified class. In addition, creates a Json file containing object representations while printing the id the object to stdout. | **create** \<class_name\>
**show**    | Prints the string representation of an instance as defined in the __str__ method. | **show** \<class_name class_id\>
**destroy** | Deletes an instance. | **destroy** \<class_name class_id\>
**all** | Prints the string representation of all instances of a class| **all** or **all** \<class_name class_id\>
**update** | Adds or modifies attribute(s) of an instance of a class | **update** \<class_name class_id key value\>
## Tests
We've created tests to verify the stability and functionality of the console and classes created. If there is a desire to run said tests, while in the AirBnB directory running the following command will execute the test modules that are in the test/test_models/ directory
```python3 -m unittest discover tests ```

<img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220304%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220304T190308Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1a5af07f000023f3cb78adfa02fe78db4f12859a22775383aa9d7fe3df78afc7" style="height:100%;width:100%" />

## Author
* **FELIPE LEÓN**
* **NELSON GALLEGO**
