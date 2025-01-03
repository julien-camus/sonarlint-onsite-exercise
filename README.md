# tasks

CLI Task Manager for SonarLint technical interviews

Copyright (C) 2023 SonarSource SA

All rights reserved

# Interview environment

The exercise consists in implementing new features for an interactive text-based task management tool.

It lasts about 3 hours with three 1-hour long "sprints". Each sprint consists of ~45-50 minutes of development and ~10-15 minutes of code reviews and feedback in-between.

Please push your full project _as is_ at least at the end of each "sprint".

# Evaluation criteria

This is _your_ product! The intention of this exercise is to help us evaluate how you would organize yourself to deliver a clean product that addresses a common need.

We will pay special attention to these criteria, by order or priority:

- Testing
- Knowledge and pragmatic application of Clean Code principles
- Ability to take decisions and make design choices based on the desirable UX
- Ability to prioritize change requests

# Tips

- Try to start simple and iterate
- Explain your work
- Relax and be yourself

# Initial specification

The task manager starts with an empty list of tasks. It reads one-line-commands and executes them. Valid commands are:

- `help`: shows a help message that describes known commands
- `show`: lists all tasks grouped by project
- `add project <project name>`: create a new project
- `add task <project name> <task description>`: add a task to a project
- `check <task ID>`: mark a task as done
- `unckeck <task ID>`: mark as task as not done 

# Example session

    > add project task-manager
    > add task task-manager Add the ability to delete a task
    > add task task-manager Add a deadline to tasks
    > show
    task-manager
        [ ] 1: Add the ability to delete a task
        [ ] 2: Add a deadline to tasks
    
    > check 1
    > show
    task-manager
        [x] 1: Add the ability to delete a task
        [ ] 2: Add a deadline to tasks
    
    > quit

# Building and running

    ./mvnw clean package appassembler:assemble
    ./target/appassembler/bin/task-list
