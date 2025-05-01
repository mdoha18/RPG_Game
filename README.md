[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/p8KCMrgr)
# OOP for AI (WBAI045-05) 2024-25 - Assignment 2

In this assignment, you'll make your own text-based RPG (Role-Playing Game). For the people who don't know what a text-based RPG is: it is an RPG that is played by interacting with a virtual world through text using a console.

In this RPG you'll be acting as the player. The game will be a sort of dungeon crawler where you make your way through all kinds of rooms, and you'll run into some of the most fantastic creatures (un)known to mankind. If you manage to reach the final room, you win eternal fame and glory (if you know how to program that).

Note that we will not explain everything in as much detail as in the first assignment. You will have to decide most of the implementation details for yourself. 

You will be continuously extending your program with new functionality, so make sure that you pay good attention to your design. The better you design your program, the easier adding new functionality will be for you.
Also, you will be asked to design some tests to check the functionality of your code.

___

## 0. Before we begin

### Deadline and submission

The deadline is set to **Sunday, October 13 2024**.
The submission has to be operated on BrightSpace by pasting the GitHub URL.
The submission on GitHub happens via **pull request**. 

### Setting up

Just as in the previous assignment, you will find the necessary files in the `rpg` branch. This means that you should make sure that you are on the `rpg` branch before you start.

This `README` is available in your group's repository. Unfortunately, we cannot update the `README` in your group's repository in case we are fixing some mistake(s) in the assignment description. As such, if you find a mistake, we will be communicating it via announcement and indicating it in the Brightspace assignment.

### Incremental Maintenance

This assignment has been divided into multiple sections so that we can focus on a small subproblem at the time. This way it is easier to manage the changes. The programs we will be writing in this course will be a lot larger than the programs written so far in other programming courses you have followed, such as Imperative Programming or Algorithms and Data Structures. Therefore, it is important to maintain a pleasant working environment. We can do this by doing the following after each step:

- Documenting your code by means of docstrings
- Running pre-commit checks to verify compliance with style guidelines
- Taking time to refactor the code
- Ensuring all tests you design are passing before progressing to the next step
- Don't overdo and plan extra functionalities that will not be needed anytime soon. Try to keep your code simple and stick to the requirements in order to avoid the coding (and, especially, testing) part to baloon out of control
- Patting yourself on the back to stay motivated


The basic idea is to get something small working as fast as possible. Then once that part works nicely, you can start working on the next requirement. After each requirement, you verify that your program still works as expected. This is important to prevent any bugs later on!

___


## 1. Rooms

Let's start with creating the most important part of our RPG: the player. We can do this by creating a class `Player`. Since we want our `Player` to have a magnificent name, the `Player` should have a field `name`.

Before we can start playing, we need something to walk around in. As mentioned before, our RPG world consists of rooms, so let's implement this by creating a class `Room`. A `Room` should have a field `description`, which will be used to `inspect` a `Room`. Whenever a `Room` is inspected, it should print this descriptive piece of text to. Later on, we will add more things to this `inspect` method.

Note that the point of having classes is (among others) reusability. Therefore, don't hardcode the room descriptions in `Room`, since this does not allow us to easily create rooms with different descriptions.
Instead, have the description string as a parameter in the constructor of `Room`. This means that wherever you initialise the `Room`, you can specify a description. This holds for almost all the classes we will be creating. In general, it is good practice to hardcode as little as possible, so try to conform to that.

Now that we have rooms and a player, we can connect the two (__relationship__ between objects). Since we play from the perspective of a `Player`, we do not let a `Room` keep track of the `Player`, but rather we let the `Player` keep track of the `Room` they are in.


**Requirements:**

- Create a `Player` class with a `name`.
- Create a `Room` class with a `description`.
- You should be able to `inspect` a `Room`. Doing so will print its description.
- The `Player` should keep track of what `Room` they are in.

## 2. A Simple Interaction Menu

We now have all the ingredients to create a basic program. Let's use the two classes mentioned above to create a simple program that can do some basic interaction. For now, you are allowed to do this in the `main.py` class, but keep in mind that this should ideally only be used for initialising. Later on, you will have to change this.

The program should print a simple options menu. The user can then enter a number that matches one of the options.
Code a `Scanner` class which is tasked with reading and validating user input.
In this part of the program, we will only have the user input positive integer numbers.
Create a `read_int` method that waits for a user to input such a number.
You can use the `input()` built-in to read a generic user input.
Note that if the user did not input a positive integer, an error should occur.

For now, let's add an option to "look around". Whenever the player looks around, the `Room` the `Player` is in should be inspected. This will look something like this:

```
What do you want to do?
  (0) Look around
0
You see: A rather dusty room full of computers.
What do you want to do?
 (0) Look around
```

As you can see, this interaction menu should keep repeating itself. For now, you can use an infinite while loop for this. Later on, we can add conditions so that the loop stops if the `Player` wins (or dies).

**Requirements:**

- A `Scanner` class, to be implemented in the `io_utils.py` script, which is tasked with reading and validating user input
- A simple interaction menu with the option to look around
- When the option `"look around"` is chosen, the `Room` the `Player` is in should be inspected.


## 3. Doors
Are you able to look around the `Room`? Well done! So far, so good. It's starting to get boring in this particular `Room` after a while though, so we decide we want to escape it and go to another `Room`. This means we will need to have doors, so let's create a class for this.

**Requirements:**

- Create a `Door` class that is very similar to a `Room`: it has a description, and you should be able to `inspect` it.

### 4. Inspectable

By now, the `behaviour` of the `Door` and `Room` classes is very similar. They both share one property: they are inspectable. Let's generalise that property!

While other programs may implement it via *interfaces*, in Python you can do so with an abstract class, called `Inspectable`, that `Door`s and `Room`s will inherit from.
Code such abstract class.
Which methods does it need to contain? Which of these are abstract?

Notice that, since `Door`s don't have an `inspect()` method, any instantiation of them should fail (if you implemented the abstract class correctly).
Thus, find the easiest way to have `Door`s instantiable while abiding to the requirements we have seen insofar.

**Requirements:**

- Create an ABC `Inspectable` with an `inspect()` method.
- `Room` should inherit from `Inspectable`.
- `Door` should inherit from `Inspectable`.


### 5. Adding Doors

It is obviously nothing short of amazing that we have added a `Door` class, but we are not doing anything with it now. That is a bit sad, so let's fix that.

A `Room` can have multiple doors. What data structure can we use to implement this?

Let's also create a method `add_door` so that we can add doors to this list.

Now that our rooms also have doors, let's extend the functionality of the `inspect` methods for rooms to also print the number of doors. Suppose our room has two doors, something like this would be shown:

```
What do you want to do?
  (0) Look around
0
You see: A rather dusty room full of computers. The room has 2 doors.
What do you want to do?
 (0) Look around
```

**Requirements:**

- Add a field `doors` to `Room` and initialize it properly.
- Add a method `add_door` to `Room` that adds a `Door` to the `doors`.
- Alter the `inspect` method of `Room` in such a way that it also prints the number of doors.


### 6. More Gameplay Options

We are also going to add another gameplay option that allows us to see all the doors in a room. The option will be "look for a way out" and, if selected, displays all the doors in the room. The user can then select a door to interact with.

Suppose that we are in a room that has two doors, this would look something like this:

```
What do you want to do?
  (0) Look around
  (1) Look for a way out
1
You look around for doors. You see:
  (0) A mysterious red door
  (1) A black door
What do you want to do?
  (0) Look around
  (1) Look for a way out
```

As you can see, the interaction is now two levels deep. Whenever the user selects "look for a way out", it will show some new interactive possibilities. We will be adding more to this interaction menu, so be sure to use separate methods (or classes!) to handle all these different possibilities. This will make it a lot easier to read and (potentially) debug your code.

If you have done the main game loop in `main.py` so far, now would be a good time to move this to a more dedicated class. You could, for example, create a class `Game` that executes the main game loop. Remember: `main.py` should only be used for initialising.


**Requirements:**

- Add an option to the interaction menu that allows the `Player` to "look for a way out".
- When the option to "look for a way out" is selected, all the `Door`s of the room should be inspected.

### 7. Entering Doors

Obviously, we want to do more than just inspecting doors. So now we are going to add something that allows the `Player` to go through a `Door`. Whenever a `Player` `interacts` with a `Door` they should go through it. This means that the `Door` will need a method `interact()`.

In order to do this, we first need to connect a `Door` to another `Room`. We can do this by adding a field to `Door` for the `Room` behind it. In this case, our doors are one-way. So once we go through it, we cannot go back (you are free to change this later on).

In the `interact()` method of `Door`, we need to somehow tell our `Player` to change rooms. However, this is a bit difficult, since the `interact()` method belongs to `Door` and not to `Player`. Therefore, you should add a parameter `Player` to the `interact()` method, so that we can tell the player to switch rooms. There is no need to make the `Player` a field everywhere or to make it a global variable, which would be even worse.

Once you added the ability for a `Player` to go through a `Door` the interaction menu should look something like this:

```
What do you want to do?
  (0) Look around
  (1) Look for a way out
0
You see: A rather dusty room full of computers and two doors.
What do you want to do?
  (0) Look around
  (1) Look for a way out
1
You look around for doors.
You see:
  (0) A mysterious red door
  (1) A black door
Which door do you take? (-1 : stay here)
1
You go through the door
What do you want to do?
  (0) Look around
  (1) Look for a way out
0
You see: A dark room with dark doors
```

**Requirements:**

- A `Door` should be connected to a `Room` behind it.
- Add an `interact()` method to `Door`. When this method is called, the player should move to the `Room` behind that `Door`.
- The `Player` should be an argument of the `interact()` method.
- The interaction menu should be augmented with an option to select a `Door` to go through after looking around.

### 8. Interactable

We have now made a `Door` interactable. However, we will also be adding more things that we can interact with (one of them being NPCs). If we wanted to expand on this program even more, we could also have chests or items to interact with. In other words, a lot of these classes would share `behaviour`. And just as before, whenever we see a lot of these (unrelated) classes sharing `behaviour`, we use an ABC.
So let's move this method into a new ABC `Interactable`.

Now `Door` can extend this class. The nice thing is, as mentioned before, that we can also use this for NPCs.

**Requirements:**

- Create an ABC `Interactable` that contains the method `interact` to interact with a `Player`.
- `Door` should extend this `Interactable` ABC.

Before we continue, let's make sure that everything works so far. Test your program to see if there are any bugs in there. As you know, if you already have a lot of bugs early on, and you continue coding your program, they will start to affect each other, and everything will be one big mess. So take it slow and you'll have an easier time.


## 9. NPCs

Now it is finally time to add some more exciting interactions to our game!

We are going to add some NPCs (Non-Player Characters). To do this, we create an `NPC` class. For now, the `NPC` should only have a field `description`. The `Player` should be able to `inspect` and `interact` with an `NPC`, so make sure `NPC` extends both `Inspectable` and `Interactable`.

An `NPC` belongs to a `Room`, so let's also create a field to keep track of all the `NPC`s in a `Room`. Note that there can be multiple `NPC`s in a room, so we can use an `List` for this.

We will add more specific NPCs later, but for now, let's use an example implementation with a simple print statement in the `interact()` method to verify that `NPC` is working. The interaction menu should be augmented with an option "look for company" which should list all the `NPC`s. This should look something like this:

```
What do you want to do?
  (0) Look around
  (1) Look for a way out
  (2) Look for company
2
You look if there’s someone here.
You see:
  (0) A suspiciously happy looking orc
  (2) The kerstman
  (3) A dancing strawberry
Interact ? (-1 : do nothing)
1
The creature is asleep so you can’t interact with it.
What do you want to do?
  (0) Look around
  (1) Look for a way out
  (2) Look for company
```
If this works, awesome! We can now start to implement some more interesting `NPC`s.

**Requirements:**

- Create an `NPC` class with a field `description`.
- An `NPC` should be `Inspectable`.
- An `NPC` should be `Interactable`.
- A `Room` should (be able to) contain several `NPC`s.
- Create a new option in the interaction menu: "Look for company".
- When the option "look for company" is chosen, it should inspect all the NPCs in the room.

## 10. A Simple Combat System

What fun is an RPG without a little combat? So let's add this!
In order to have combat, we first need something to fight. So let's create an `Enemy` class. Since `Enemy` is an `NPC`, it should extend from `NPC`.

From now on, you will have to make the design decisions yourself. We will only give some requirements that your program should have and you are free to decide how to implement this. Try to make use of inheritance, abstract classes, and interfaces to create a proper design here!

Take into considerations that:

- A combat will likely require a specific interaction menu, which allows the player to choose *at least* the options of (0) attacking or (1) running away.
- You should work out a damage computation system which allows the `Player`, on average, to survive most fights.

**Requirements:**

- `Player` should have damage and health.
- All `NPC`s should have damage and health.
- Only `Player` and `Enemy` should be attackable.
- The `Player` should be able to attack an `Enemy` and by doing this deal damage to that `Enemy`.
- An `Enemy` should be able to attack the `Player` and by doing this deal damage to the `Player`.
- The `Player` or an `NPC` should die when its health drops to or below 0.
- The game stops when the `Player` dies. When the game stops, it should print something along the lines of "Game Over!".
- A simple interaction menu for the combat. For example, when the `Player` interacts with an `Enemy` it should give the option to attack that enemy. The `Enemy` then attacks back etc.

## 11. Add other NPC classes

You should add *at least* another NPC class. This class should extend `NPC` and have a different behaviour than the `Enemy`. Examples might be healing NPCs. You are free to choose what you want to add, but make sure that it is different from the `Enemy` class.


## 12. Saving

In many programs, we can save data. The program does this by writing certain information to a file. Abstractly speaking, it is converting program data into a structured form, so that it can be converted back into the program data later.
This conversion of program data to structured data (saving) is referred to as serialization. The reverse process (loading) is called de-serialization. There are some formats available that store information in an organized manner such as YAML, JSON or XML. In this case, we will pick JSON as destination file.

In the next few parts, we will make use of serialization to make save files. This way, we can have (quick)saving and (quick)loading in our game.

### JsonSerializable

While some objects (ints, strings) in Python are already natively JSON-serializable, some of them, like custom classes, are not.
We need to tell Python how to serialize them, which is done by having them implement a method `toJSON`.
This method implements the basic rules for saving the object as a JSON file.

We will be marking an object as JSON-serializable by means of base class called `JsonSerializable`, which should indicate that the object is serializable and is part of a save file.
You are tasked with identifying whether this class needs to be abstract or if it can be implemented as a concrete method.

A JSON-serializable object needs to have all of its serializable attributes dumped to a JSON.
In Python, the following types are natively JSON-serializable:

- int
- float
- str
- bool
- None
- Collections (list, dict, tuple)

If we want to serialize other objects in the context of our code, they need to extend `JsonSerializable`.

When saving an class (calling `toJSON`), you will need to indicate that all of its serializable attributes be saved.
Do it in an elegant way, by calling a `JsonSerializable` type check and checking for the aforementioned natively JSON-serializable types.

**Requirements:**

- Make every class you want to save extend `JsonSerializable`.

## 13. Loading

After implementing saving, you should implement a functionality to load from a JSON file.
In this case, you should add a `fromJSON` method in `JsonSerializable` and code the logics so that an instance can be recreated from the JSON description.
_Notice: the choice is yours on whether to implement a concrete `toJSON` in the ABC or to have one implemented on each class._

### 14. New interact options

Before we start with the actual saving and loading, we are first going to add two options to the interaction menu: `QuickSave` and `QuickLoad`.
This will look something like this:

```
What do you want to do?
  (0) Look around
  (1) Look for a way out
  (2) Look for company
  (3) QuickSave
  (4) QuickLoad
```

For now, these actions do not need to do anything, but we are going to use them in a bit.

**Requirements:**

- Add an option `QuickSave` to the interaction menu.
- Add an option `QuickLoad` to the interaction menu.

### 15. Quicksaving and Quickloading

Now that we have set up our classes to be saved, it is time to move on to the actual saving part. Create a `Saver` class in `io_utils.py`.

We want to store our saves in a directory called `savedgames` and this directory should be located in the root of this assignment directory.
Now we need to ensure that this directory is created if it does not exist yet. To achieve this, you can make use of the `os` library, which has a host of useful functions (e.g., `os.path.isdir` or `os.makedirs`).

Whenever the user chooses the option `QuickSave`, the program should save the state of the game in a file called `quicksave.json` inside of this `savedgames` directory.
You can do so using the `json` library, which has a `dump` method that can be used to write a JSON file.

Whenever the user chooses the option `QuickLoad`, the program should load the state of the game as it was saved in the file `quicksave.json`.

We need to make sure that we give appropriate feedback to the user if something went wrong (for example if the file does not exist). Usually, a simple print statement should be enough. While printing the stack trace might be very useful for debugging, we do not want this in our final program, since we do not want our users to see this. Always give proper feedback to the user if something goes wrong.

**Requirements:**

- Save games should be stored in a directory called `savedgames` at the root of the assignment directory.
- The `savedgames` directory should be created if it does not exist yet.
- Choosing `QuickSave` should save the game in a file called `quicksave.ser`.
- Choosing `QuickLoad` should load the game as it was saved in the file `quicksave.ser`
- If something goes wrong during saving or loading, the program should print an informative message to the user.

**Functionality Warning**:
It could very well be that something broke because of the saving and loading process. Therefore, be sure to verify that all your program features still work after loading a game.

## 16. Error handling

At this point, your program hopefully works as you intend it to work. However, what if the user does something stupid? For example, the user tries to input a menu option that does not exist or the user entered a filename that might produce errors. Make sure to have proper error handling for these kinds of scenarios. With proper error handling, we simply mean that you should inform the user that something went wrong and that (if possible) the program should keep running.

Remember that you should not have empty try/catch statements! Having empty catches is a very bad practice because you are hiding the fact that an error occurred and continuing execution as normal. It is essentially equivalent to putting a piece of tape on an engine warning light. If something goes wrong, you have no idea where it went wrong and why, so you are strongly recommended to inform the user when something does go wrong and an exception is thrown.

Not only is it important that your program has all the functionality, but it should also be able to handle exceptional scenarios. As such, it is very important to test your program for these kinds of scenarios. This also prevents the situation of you encountering an exception for the first time during the demo and having to say "I have not seen that before (◔ д◔)".

**Requirements:**

- Thoroughly add proper error handling.

## 17. Testing

This assignment is basically piecing together multiple of the concepts studied insofar.
Besides the OOP concepts, with which you should be relatively familiar by now, you should also be able to write tests for your code.
You should write the following sets of tests:

- Unit tests for all the classes and methods you have created. Remember that unit tests check behaviors in isolation, so you should mock the dependencies of the classes you are testing, if there are some.
- Integration tests for the main game loop. This is a bit more difficult, as you will have to test the interaction between different classes. 
- *At least* one functional test that runs a game from start to finish and checks if everything works as expected.



___

# Additional notes

## 1. Randomness

**As an indication, there should be at least one part of the code that includes randomness, be it in the damage calculation, or in the probability to run away from a battle, or even in the setup of a room.**
Remember to add tests for these parts of the code, using one or more strategies as from the lectures.

## 2. Workload suggestions

As you can notice, this assignment is more complex than assignment 1: as such, you will be required a bit more workload organization for it.
We suggest you to start working on it straight away, so that points 1-10 are handled during the first week, and the remainder is handled during the second week.
Specifically, for point 17. (testing), you will be able to have some additional insights from Tutorial II, which will be held on October 7th, and for points 12. and 13. (saving and loading), you can apply what we will learn in Lecture 09 (October 4th).


## 3. Be Creative!

You are encouraged to add your own twist to the RPG! Create a real story or make the experience more enjoyable in whatever way you wish. Once you get the hang of it, it will be a lot of fun to think of new things and functionalities to add!
Think of fairies, trolls, weird items, characters from Lord of the Rings - the more interesting the story and the game, the more chance you have at getting bonus points! Just make sure that your program can at least do what is specified in the requirements. Also, be sure to keep paying attention to the design of your program. While a very nice game is obviously amazing, we will be mainly looking at your code/design.

___

## Folder structure

- At the root of the repo, you should have the following files:
  - `main.py` where you initialize the game
  - `.gitignore`. If you use a **virtual environment within the repo**, remember to **add its folder** to this file. **Unnecessary stuff that doesn't need to be pushed in the repo and is not currently in the .gitignore should be added here by you**.
  - `requirements.txt` for installing libraries useful for your code execution (to be populated by you).
  - `README.md` containing these instructions. Do not touch this file.
  - Optionally, you may add a `report.md` for reporting your style and coding choices.
- Additionally, there should be two other folders.
  - A `.github` folder where the code for GitHub actions are stored.
  - The `rpg` folder containing the library scripts (you will find some empty scripts at the beginning). **This folder should contain no subfolders**.



## Grading information

| Category      | Max points    |
| ------------- |:-------------:|
| Functionality | 4             |
| Design        | 3             |
| Testing       | 3             |

Concerning design, as for assignment 1, we will be looking at:

- Correct application of OOP principles (encapsulation, inheritance, polymorphism)
  - Hence, correct choice of private/public attributes/methods is paramount
  - Be careful at leakage too
- Correct folder structure
  - This includes the fact that the correct files were pushed on the repo. Pushing extra files (such as virtual environments) will cause a penalty of up to 1 pt per wrong file/folder
- Style choices:
  - Documentation (missing docstrings will cause a deduction of 0.25 pts each)
  - `flake8` style violations will be penalized by 0.25 each (according to automatic tests—not pre-commit checks)
  - Naming conventions (such as camelCase for attribute, methods, and file names) will be penalized by 0.5 pts each
  - Bloaters such as long methods and long class will be penalized by up to 0.5 pts each
  - Meaningless/uninformative/misleading variable names will be penalized up to 0.25 pts each
  - Missing typing will be penalized by 0.5 pts each.
- Overdue day: for each overdue day (rounded up), 1 pt. will be deducted.


