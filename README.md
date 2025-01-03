# cli-calculator

CLI Calculator for SonarLint technical interviews

Copyright (C) 2021 SonarSource SA

All rights reserved

# Exercise

The exercise consists in implementing an interactive text-based command line calculator.

The calculator starts with a "current" value of 0. It reads one-line-commands and executes them. Valid commands are:

- `ADD <OPERAND>`: add the value of operand to the current value
- `SUBTRACT <OPERAND>`: subtract the value of operand from the current value
- `MULTIPLY BY <OPERAND>`: multiply the current value by the value of operand
- `DIVIDE BY <OPERAND>`: divide the current value by the value of the operand
- `DISPLAY`: show the list of values computed since the last call to DISPLAY

# Example session

In the example below, `>` marks user input and `<` marks calculator output:

    > ADD 5
    > MULTIPLY BY 3
    > SUBTRACT 3
    > DISPLAY
    < 5
    < 15
    < 12
    > DIVIDE BY 6
    > DISPLAY
    < 2

# Evaluation criteria

- Knowledge and pragmatic application of SOLID principles
- Testing
- Ability to take decisions and make design choices based on the desirable UX
- Ability to prioritize change requests

# Interview environment

The exercise lasts about 3 hours with three 1-hour long "sprints". Each sprint consists of ~45-50 minutes of development and ~10-15 minutes of code reviews and feedback in-between.

Please push your full project _as is_ at least at the end of each "sprint".
