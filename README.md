# sov_lang 0.2.1
Python based "programming language" created for basic logic gate simulations.

Usage
=
1. Download both compiler.py and lib.py and save them in the same directory
```
git init
git pull https://github.com/k0ryan/sov_lang
```
2. Compile your code with:
```
python3 compile.py example.sov
```
3. Edit or check your code in example.py
4. Run compiled file
```
python3 example.sov
```

Syntax
=

Variables
-
There are two types of **variables**:
1. The ones you want to define when it runs
```
in
  input0
  input1
in.
```
2. The ones that won't be changed by the user
```
var
  output0
  output1
var.
```

The first type is used as an input while the second ones are used as a buffer to connect gates.

Gates
-
To create two **gates** you want to:
```
and0
  input0
  input1
  output0
and.

and1
  input2
  output0
  output1
and.
```

As you can see the first "and" takes input0 and input1 and saves the result in output0.
Then the second "and" takes input2 and the output from last gate and saves the result in ouput1.

You can create the following **gates** for now:
* and
* nand
* or
* nor

You must give different **names** to the gates. The only requirement for naming gates is that they contain the actual name of the gate.
Example:
```
and0
and_
andc
anda
andb
```

Other instructions
-
To **print** any variable:
```
print
  output0
  output1
  input0
  input1
  whatever
print.
```
