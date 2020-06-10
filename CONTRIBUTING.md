# Contribution guidelines
**Important**:
1. Please do not commit directly to the master branch, but instead, commit your work to a separate branch.
2. Send a pull request to merge the changes from your branch to the master branch.
3. While sending a pull request, briefly explain the changes you have made.

Before sending pull requests from your branch, make sure that you **read the whole guidelines**. If you have any doubts or suggestions about the contribution guidelines, feel free to [create an issue](https://github.com/harshildarji/TMP-SS-2020/issues/new).

## Structure
As mentioned in the TMP topic ideas document, make sure to structure your repository in the following way:
```
root/
|-- code/
|-- intermediate-reports/
|-- literature/
|-- project-report/
|-- presentation/
|-- README.md
```
- README file in the root directory is only to provide a general description of the project and key ideas.
- To provide instruction on how to set up the code, create another README.md in the code directory.
- Make use of [`.gitignore`](https://git-scm.com/docs/gitignore) to avoid pushing configuration files or directories.

## Coding style
Since this repository will be maintained by three collaborators, it is necessary to follow some common rules to avoid any issues.

- Please write in **`Python 3.7+`**.
- Please pay attention to naming functions, classes, and variables. If possible, make use of **descriptive names**.

  - Single letter variable names are bad for readability, so please refrain from using them unless their life only spans a few lines (_for example, in loops_).
  - Please avoid using acronyms in method names (_for example, it is better to use `greatest_common_divisor()` than just `gcd()`_).
  - Please follow [Python Naming Conventions](https://pep8.org/#prescriptive-naming-conventions).
  
- Make sure your submission pass the test **`flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics`** before sending the pull request. So if possible, try this test locally before submitting the pull request.
  ```
  pip3 install flake8
  flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
  ```
  Some information on above mentioned error codes:
  
  - **E9**: These tests are usually about Python _SyntaxError_, _IndentationError_, or _IOError_. For more info, visit [PEP8 Error codes](https://pep8.readthedocs.io/en/release-1.7.x/intro.html#error-codes).
  - **F63**: These tests are usually about the _confusion between identity and equality_ in Python.
  - **F7**: These tests are for _logical or syntax errors in type hints_.
  - **F82**: These tests are almost always for _undefined names_ which are usually a sign of a typo, missing imports, or code that has not been ported to Python 3.
  
- Please make sure to use [docstrings](https://www.python.org/dev/peps/pep-0257/) to describe your work.

---
#### New guidelines might be added as the project progresses.
