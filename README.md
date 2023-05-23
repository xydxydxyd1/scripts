Overview
========
My personal scripts folder; mostly for backup and quick deployment

Scripts
=======

#### cmakeinit ####
```
Name: cmakeinit

Synopsis: cmakeinit

Description:
    Sets up a working environment with CMake and git in the current directory

    Initialize CMakeLists.txt with my default settings:
        cmake_minimum_required: 3.22
        project name: working directory name
        CMAKE_EXECUTABLE_SUFFIX .out
        CMAKE_CXX_STANDARD 17
        CMAKE_CXX_STANDARD_REQUIRED True
        CMAKE_EXPORT_COMPILE_COMMANDS ON
```

#### csif ####
```
Name: csif

Synopsis: csif OPTIONS...

Description:
    SSH into my school computers and mount the remote drive at ~/remote
    
    -t
        SFTP instead of SSH, does not mount remote.

    -s
        Only check the remote status

    -n
        SSH without mounting drive
```

#### ezcommit ####
```
Name: ezcommit

Synopsis: ezcommit STRING

Description:
    git add -A
    git commit -m STRING
```

#### ezmerge ####
```
Name: ezmerge

Synopsis: ezmerge

Description:
    Push the current branch, merge to remote, update local main,
    and then delete the current branch.
```

#### firstpush ####
```
Name: firstpush

Synopsis: firstpush

Description:
    git push --set-upstream origin current_branch
```

#### hwtest ####
```
Name: hwtest

Synopsis: hwtest test_case_num

Description:
    run build/main with input/#.txt, check against expected/#.txt
```

#### lcovgen ####
```
Name: lcovgen

Synopsis: lcovgen

Description:
    Generate captured code coverage report
```

#### lcovinit ####
```
Name: lcovinit

Synopsis: lcovinit

Descrption:
    Begin capturing code coverage in ./build/
```

#### newsh ####
```
Name: newsh

Synopsis: newsh FILENAME

Description:
    Set up a new shellscript named FILENAME, initialized with basic
    argument validation and execution permission
```

#### regex ####
```
Name: regex

Synopsis: regex REGEX_EXPRESSION STRING

Description:
    Checks if the expression matches the string.
```

#### run ####
```
Name: run

Synopsis: `run [-x language] [-g] FILE`

Description:
    Quickly run and build FILE.

    When running assembly, automatically starts gdb

    -x language
        Compile with specified language.
        Supported: cxx, asm

    -g
        For cxx: instead of running normally, run in gdb.
```

#### sshmount ####
```
Name: sshmount

Synopsis: sshmount HOST [SSH_OPTIONS]

Description:
    Opens an SSH connection with HOST and mount the remote home folder on
    ~/remote/HOST/

Author:
    https://github.com/wd5gnr
```

#### testscript ####
```
Name: testscript

Synopsis: testscript

Description:
    Prints "the scripts folder is linked!"; used for checking if scripts
    are added to PATH
```
