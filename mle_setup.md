Script started on Sun Apr 27 19:03:18 2025
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(base) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h/usr/bin/python3 /Users/satishgundu/.vscode/extensions/ms-python.python-2025.4.0-darwin-arm64/python_files/printEnvVariablesToFile.py /Users/satishgundu/.vscode/extensions/ms-python.python-2025.4.0-darwin-arm64/python_files/deactivate/zsh/envVars.txt[K[A[80Dclear[K[1B[K[A[63Cconda deactivate[16Dpython3.13 -m pip install --upgrade pip[33D --version                       [23D[10D3.13 -m pip install --upgrade pip[39Dconda deactivate                       [23D[16Dclear           [11Dconda deactivate[16Dpython3.13 -m pip install --upgrade pip                                p  python --version[16Dpip install pylint flake8 black isort[37Dgit status                           [27D[10Dpip install pylint flake8 black isort[37Dgit status                           [27Dcheckout -b setup/python-tools[30Dstatus                        [24D[10Dpip install pylint flake8 black isort[37Dpython --version                     [21D[16D                [16Dccat bad_code.py[1m [0m[0m [?2004l[1Bimport sys,os

def add(x,y):
 return x+y

def sub(x,y):return x-y

def multiply(x,y):
    z= x* y
    return z
def divide(x,y):return x/y

print("Addition:",add(10,5))
print("Subtraction:",sub(10,5))
print("Multiplication:",multiply(10,5))
print("Division:",divide(10,5))[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(base) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[H[2J[0m[27m[24m[J(base) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(base) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(base) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hcat bad_code.py[15D/usr/bin/python3 /Users/satishgundu/.vscode/extensions/ms-python.python-2025.4.0-darwin-arm64/python_files/printEnvVariablesToFile.py /Users/satishgundu/.vscode/extensions/ms-python.python-2025.4.0-darwin-arm64/python_files/deactivate/zsh/envVars.txt[K[K       [?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(base) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hfflake8 bad_code.py[1m [0m[0m [?2004l
[1mbad_code.py[m[36m:[m1[36m:[m1[36m:[m [1m[31mF401[m 'sys' imported but unused
[1mbad_code.py[m[36m:[m1[36m:[m1[36m:[m [1m[31mF401[m 'os' imported but unused
[1mbad_code.py[m[36m:[m1[36m:[m11[36m:[m [1m[31mE401[m multiple imports on one line
[1mbad_code.py[m[36m:[m1[36m:[m11[36m:[m [1m[31mE231[m missing whitespace after ','
[1mbad_code.py[m[36m:[m3[36m:[m1[36m:[m [1m[31mE302[m expected 2 blank lines, found 1
[1mbad_code.py[m[36m:[m3[36m:[m10[36m:[m [1m[31mE231[m missing whitespace after ','
[1mbad_code.py[m[36m:[m4[36m:[m2[36m:[m [1m[31mE111[m indentation is not a multiple of 4
[1mbad_code.py[m[36m:[m6[36m:[m1[36m:[m [1m[31mE302[m expected 2 blank lines, found 1
[1mbad_code.py[m[36m:[m6[36m:[m10[36m:[m [1m[31mE231[m missing whitespace after ','
[1mbad_code.py[m[36m:[m6[36m:[m13[36m:[m [1m[31mE231[m missing whitespace after ':'
[1mbad_code.py[m[36m:[m8[36m:[m1[36m:[m [1m[31mE302[m expected 2 blank lines, found 1
[1mbad_code.py[m[36m:[m8[36m:[m15[36m:[m [1m[31mE231[m missing whitespace after ','
[1mbad_code.py[m[36m:[m9[36m:[m6[36m:[m [1m[31mE225[m missing whitespace around operator
[1mbad_code.py[m[36m:[m9[36m:[m9[36m:[m [1m[31mE225[m missing whitespace around operator
[1mbad_code.py[m[36m:[m11[36m:[m1[36m:[m [1m[31mE302[m expected 2 blank lines, found 0
[1mbad_code.py[m[36m:[m11[36m:[m13[36m:[m [1m[31mE231[m missing whitespace after ','
[1mbad_code.py[m[36m:[m11[36m:[m16[36m:[m [1m[31mE231[m missing whitespace after ':'
[1mbad_code.py[m[36m:[m13[36m:[m1[36m:[m [1m[31mE305[m expected 2 blank lines after class or function definition, found 1
[1mbad_code.py[m[36m:[m13[36m:[m18[36m:[m [1m[31mE231[m missing whitespace after ','
[1mbad_code.py[m[36m:[m13[36m:[m25[36m:[m [1m[31mE231[m missing whitespace after ','
[1mbad_code.py[m[36m:[m14[36m:[m21[36m:[m [1m[31mE231[m missing whitespace after ','
[1mbad_code.py[m[36m:[m14[36m:[m28[36m:[m [1m[31mE231[m missing whitespace after ','
[1mbad_code.py[m[36m:[m15[36m:[m24[36m:[m [1m[31mE231[m missing whitespace after ','
[1mbad_code.py[m[36m:[m15[36m:[m36[36m:[m [1m[31mE231[m missing whitespace after ','
[1mbad_code.py[m[36m:[m16[36m:[m18[36m:[m [1m[31mE231[m missing whitespace after ','
[1mbad_code.py[m[36m:[m16[36m:[m28[36m:[m [1m[31mE231[m missing whitespace after ','
[1mbad_code.py[m[36m:[m16[36m:[m32[36m:[m [1m[31mW292[m no newline at end of file
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(base) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hiisort bad_code.py[1m [0m[0m [?2004l
Fixing /Users/satishgundu/Documents/2.2025/ultimate-devops-project-demo-main/mle-project/python-mle-setup/bad_code.py
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(base) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hccat bad_code.py[1m [0m[0m [?2004l
import os
import sys


def add(x,y):
 return x+y

def sub(x,y):return x-y

def multiply(x,y):
    z= x* y
    return z
def divide(x,y):return x/y

print("Addition:",add(10,5))
print("Subtraction:",sub(10,5))
print("Multiplication:",multiply(10,5))
print("Division:",divide(10,5))[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(base) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hddiff cat     d  ccle c  cat bad_code.py[15Disort bad_code.py[P[11C [12D[P[11C [12D[P[11C [12D[P[11C [12Di[P[11C [12D[P[11C [12Dbbad_code.py[11Dblbad_code.py[11Dabad_code.py[11Dcbad_code.py[11Dkbad_code.py[11D bad_code.py[11D[1C[1C[1C[1C[1C[1C[1C[1C[1C[1C[1C[?2004l
[1mreformatted bad_code.py[0m

[1mAll done! ✨ 🍰 ✨[0m
[34m[1m1 file [0m[1mreformatted[0m.
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(base) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hccat bad_code.py[1m [0m[0m [?2004l
import os
import sys


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multiply(x, y):
    z = x * y
    return z


def divide(x, y):
    return x / y


print("Addition:", add(10, 5))
print("Subtraction:", sub(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(base) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[7mpip install pylint[27m[18D[27mp[27mi[27mp[27m [27mi[27mn[27ms[27mt[27ma[27ml[27ml[27m [27mp[27my[27ml[27mi[27mn[27mt[?2004l

[1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m A new release of pip is available: [0m[31;49m24.3.1[0m[39;49m -> [0m[32;49m25.1[0m
[1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m To update, run: [0m[32;49mpython3.13 -m pip install --upgrade pip[0m
[1;31merror[0m: [1mexternally-managed-environment[0m

[31m×[0m This environment is externally managed
[31m╰─>[0m To install Python packages system-wide, try brew install
[31m   [0m xyz, where xyz is the package you are trying to
[31m   [0m install.
[31m   [0m 
[31m   [0m If you wish to install a Python library that isn't in Homebrew,
[31m   [0m use a virtual environment:
[31m   [0m 
[31m   [0m python3 -m venv path/to/venv
[31m   [0m source path/to/venv/bin/activate
[31m   [0m python3 -m pip install xyz
[31m   [0m 
[31m   [0m If you wish to install a Python application that isn't in Homebrew,
[31m   [0m it may be easiest to use 'pipx install xyz', which will manage a
[31m   [0m virtual environment for you. You can install pipx with
[31m   [0m 
[31m   [0m brew install pipx
[31m   [0m 
[31m   [0m You may restore the old behavior of pip by passing
[31m   [0m the '--break-system-packages' flag to pip, or by adding
[31m   [0m 'break-system-packages = true' to your pip.conf file. The latter
[31m   [0m will permanently disable this error.
[31m   [0m 
[31m   [0m If you disable this error, we STRONGLY recommend that you additionally
[31m   [0m pass the '--user' flag to pip, or set 'user = true' in your pip.conf
[31m   [0m file. Failure to do this can result in a broken Homebrew installation.
[31m   [0m 
[31m   [0m Read more about this behavior here: <https://peps.python.org/pep-0668/>

[1;35mnote[0m: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
[1;36mhint[0m: See PEP 668 for the detailed specification.
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(base) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hpip install pylint[18Dcat bad_code.py   [15Dblack bad_code.py              b  cat bad_code.py[15Disort bad_code.py              i  lls[?2004l
bad_code.py		mle_setup.md		README.md		requirements.txt
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(base) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hlspip install pylint[18Dcat bad_code.py   [15Dblack bad_code.py[17Dcat[P[P[12C  [15Disort bad_code.py[17Dflake8 bad_code.py[18Dcat[3P[12C   [15D/usr/bin/python3 /Users/satishgundu/.vscode/extensions/ms-python.python-2025.4.0-darwin-arm64/python_files/printEnvVariablesToFile.py /Users/satishgundu/.vscode/extensions/ms-python.python-2025.4.0-darwin-arm64/python_files/deactivate/zsh/envVars.txt[K[A[80Dcat bad_code.py[K[1B[K[A[73C[15Dflake8 bad_code.py[18Disort[P[12C [17Dca[P[P[13C  [15Dblack bad_code.py[17Dcat[P[P[12C  [15Dpip install pylint[18Dcat bad_code.py   [15Dpip install pylint              p  cat bad_code.py[15Dblack bad_code.py[17Dcat[P[P[12C  [15Disort bad_code.py[17Dflake8 bad_code.py[18Dcat[3P[12C   [15D/usr/bin/python3 /Users/satishgundu/.vscode/extensions/ms-python.python-2025.4.0-darwin-arm64/python_files/printEnvVariablesToFile.py /Users/satishgundu/.vscode/extensions/ms-python.python-2025.4.0-darwin-arm64/python_files/deactivate/zsh/envVars.txt[K[A[80Dclear[K[1B[K[A[63Cconda deactivate[16Dpython3.13 -m pip install --upgrade pip[33D --version                       [23D[16Dpip install pylint flake8 black isort[37Dgit status                           [27D       g  cconda act  activate /opt/anaconda3[1m/[0m[0m/envs[1m/[0m[0m/mle-env[1m/[0m[0m [?2004l[1Busage: conda [-h] [-v] [--no-plugins] [-V] COMMAND ...
conda: error: argument COMMAND: invalid choice: 'aactivate' (choose from 'activate', 'clean', 'commands', 'compare', 'config', 'create', 'deactivate', 'env', 'export', 'info', 'init', 'install', 'list', 'notices', 'package', 'build', 'content-trust', 'convert', 'debug', 'develop', 'doctor', 'index', 'inspect', 'metapackage', 'render', 'repoquery', 'skeleton', 'repo', 'pack', 'token', 'server', 'remove', 'uninstall', 'rename', 'run', 'search', 'update', 'upgrade')
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(base) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hconda aactivate /opt/anaconda3/envs/mle-env v[1m/[0m[0m [P[35C [36D[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[H[2J[0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [Kconda activate /opt/anaconda3/envs/mle-env[35Dactivate /opt/anaconda3/envs/mle-env[43Dls                                         [41Dpip install pylint[18Dcat bad_code.py   [15Dblack bad_code.py[?2004l
[1mAll done! ✨ 🍰 ✨[0m
[34m1 file [0mleft unchanged.
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hccat bad_code.py[1m [0m[0m [?2004l
import os
import sys


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multiply(x, y):
    z = x * y
    return z


def divide(x, y):
    return x / y


print("Addition:", add(10, 5))
print("Subtraction:", sub(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hcclear[?2004l
[H[2J[3J[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hppip install fla           p  fflake8    ke8 cat   bad_code.py[1m [0m[0m [?2004l
[1mbad_code.py[m[36m:[m1[36m:[m1[36m:[m [1m[31mF401[m 'os' imported but unused
[1mbad_code.py[m[36m:[m2[36m:[m1[36m:[m [1m[31mF401[m 'sys' imported but unused
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[7mpylint bad_code.py[27m[18D[27mp[27my[27ml[27mi[27mn[27mt[27m [27mb[27ma[27md[27m_[27mc[27mo[27md[27me[27m.[27mp[27my[?2004l
zsh: command not found: pylint
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hcconda install pylint[?2004l
Channels:
 - defaults
Platform: osx-arm64
Collecting package metadata (repodata.json): - \ | / done
Solving environment: \ done

## Package Plan ##

  environment location: /opt/anaconda3/envs/mle-env

  added / updated specs:
    - pylint


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    astroid-3.3.8              |  py310hca03da5_0         553 KB
    dill-0.3.8                 |  py310hca03da5_0         178 KB
    pylint-3.3.5               |  py310hca03da5_0         1.1 MB
    tomlkit-0.13.2             |  py310hca03da5_0          86 KB
    ------------------------------------------------------------
                                           Total:         1.9 MB

The following NEW packages will be INSTALLED:

  astroid            pkgs/main/osx-arm64::astroid-3.3.8-py310hca03da5_0 
  dill               pkgs/main/osx-arm64::dill-0.3.8-py310hca03da5_0 
  pylint             pkgs/main/osx-arm64::pylint-3.3.5-py310hca03da5_0 
  tomlkit            pkgs/main/osx-arm64::tomlkit-0.13.2-py310hca03da5_0 
  typing-extensions  pkgs/main/osx-arm64::typing-extensions-4.12.2-py310hca03da5_0 


Proceed ([y]/n)? y


Downloading and Extracting Packages:
pylint-3.3.5         | 1.1 MB    |                                                                                                                                 |   0% 
astroid-3.3.8        | 553 KB    |                                                                                                                                 |   0% [A

dill-0.3.8           | 178 KB    |                                                                                                                                 |   0% [A[A


tomlkit-0.13.2       | 86 KB     |                                                                                                                                 |   0% [A[A[Apylint-3.3.5         | 1.1 MB    | #7                                                                                                                              |   1% 

dill-0.3.8           | 178 KB    | ###########4                                                                                                                    |   9% [A[A
astroid-3.3.8        | 553 KB    | ###6                                                                                                                            |   3% [A


tomlkit-0.13.2       | 86 KB     | #######################6                                                                                                        |  19% [A[A[A


tomlkit-0.13.2       | 86 KB     | ############################################################################################################################### | 100% [A[A[A

dill-0.3.8           | 178 KB    | ############################################################################################################################### | 100% [A[A


tomlkit-0.13.2       | 86 KB     | ############################################################################################################################### | 100% [A[A[A

dill-0.3.8           | 178 KB    | ############################################################################################################################### | 100% [A[Apylint-3.3.5         | 1.1 MB    | ##########################################################################3                                                     |  59% 
astroid-3.3.8        | 553 KB    | #################################################################################################################8              |  90% [A
astroid-3.3.8        | 553 KB    | ############################################################################################################################### | 100% [Apylint-3.3.5         | 1.1 MB    | ############################################################################################################################### | 100% 
astroid-3.3.8        | 553 KB    | ############################################################################################################################### | 100% [Apylint-3.3.5         | 1.1 MB    | ############################################################################################################################### | 100% pylint-3.3.5         | 1.1 MB    | ############################################################################################################################### | 100%                                                                                                                                                                           
                                                                                                                                                                          [A

                                                                                                                                                                          [A[A


                                                                                                                                                                          [A[A[A
Preparing transaction: - done
Verifying transaction: | / done
Executing transaction: \ | done
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hcclear[?2004l
[H[2J[3J[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hclearconda install pylint[20Dpylint bad_code.py  [?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[7mpylint --generate-rcfile > .pylintrc[27m[36D[27mp[27my[27ml[27mi[27mn[27mt[27m [27m-[27m-[27mg[27me[27mn[27me[27mr[27ma[27mt[27me[27m-[27mr[27mc[27mf[27mi[27ml[27me[27m [27m>[27m [27m.[27mp[27my[27ml[27mi[27mn[27mt[27mr[27mc[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hllsv-la     -la[?2004l
total 128
drwxr-xr-x@  9 satishgundu  staff    288 Apr 27 19:31 .
drwxr-xr-x@  7 satishgundu  staff    224 Apr 27 19:14 ..
drwxr-xr-x@ 13 satishgundu  staff    416 Apr 27 18:58 .git
-rw-r--r--@  1 satishgundu  staff   3443 Apr 26 19:45 .gitignore
-rw-r--r--@  1 satishgundu  staff  21800 Apr 27 19:31 .pylintrc
-rw-r--r--@  1 satishgundu  staff    318 Apr 27 19:14 bad_code.py
-rw-r--r--@  1 satishgundu  staff  24477 Apr 27 19:31 mle_setup.md
-rw-r--r--@  1 satishgundu  staff   2388 Apr 26 19:45 README.md
-rw-r--r--@  1 satishgundu  staff    167 Apr 26 20:17 requirements.txt
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hls -lapylint --generate-rcfile > .pylintrc[36Dclear                               [31Dconda install pylint[20Dpylint bad_code.py  [?2004l
************* Module bad_code
bad_code.py:1:0: C0114: Missing module docstring (missing-module-docstring)
bad_code.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
bad_code.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
bad_code.py:13:0: C0116: Missing function or method docstring (missing-function-docstring)
bad_code.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 6.67/10

[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hccat bad_code.py[1m [0m[0m [?2004l
import os
import sys


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multiply(x, y):
    z = x * y
    return z


def divide(x, y):
    return x / y


print("Addition:", add(10, 5))
print("Subtraction:", sub(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[H[2J[0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [Kcat bad_code.py[15Dpylint bad_code.py[?2004l
************* Module bad_code
bad_code.py:14:4: W0107: Unnecessary pass statement (unnecessary-pass)
bad_code.py:21:4: W0107: Unnecessary pass statement (unnecessary-pass)
bad_code.py:28:4: W0107: Unnecessary pass statement (unnecessary-pass)
bad_code.py:31:19: E0602: Undefined variable 'add' (undefined-variable)
bad_code.py:32:22: E0602: Undefined variable 'sub' (undefined-variable)
bad_code.py:33:25: E0602: Undefined variable 'multiply' (undefined-variable)
bad_code.py:34:19: E0602: Undefined variable 'divide' (undefined-variable)

------------------------------------------------------------------
Your code has been rated at 0.00/10 (previous run: 6.67/10, -6.67)

[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hpylint bad_code.py[18Dca[3P[13C   [15Dpylint bad_code.py[?2004l
************* Module bad_code
bad_code.py:3:0: C0301: Line too long (121/88) (line-too-long)
bad_code.py:65:0: C0304: Final newline missing (missing-final-newline)

------------------------------------------------------------------
Your code has been rated at 8.82/10 (previous run: 0.00/10, +8.82)

[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hpylint bad_code.py[18Dca[3P[13C   [15Dpylint bad_code.py[P[11C [12D[P[11C [12D[P[11C [12D[P[11C [12D[P[11C [12Dp[P[11C [12D[P[11C [12Dbbad_code.py[11Dblbad_code.py[11Dabad_code.py[11Dcbad_code.py[11Dkbad_code.py[11D bad_code.py[11D[?2004l
[1mreformatted bad_code.py[0m

[1mAll done! ✨ 🍰 ✨[0m
[34m[1m1 file [0m[1mreformatted[0m.
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hblack bad_code.py[17Dpylint bad_code.py[18Dca[3P[13C   [15Dpylint bad_code.py[18Dls -la            [12Dpylint --generate-rcfile > .pylintrc[36Dclear                               [31Dconda install pylint[20Dpylint bad_code.py  [18Dflake8[12C[?2004l
[1mbad_code.py[m[36m:[m3[36m:[m80[36m:[m [1m[31mE501[m line too long (121 > 79 characters)
[1mbad_code.py[m[36m:[m6[36m:[m1[36m:[m [1m[31mF401[m 'os' imported but unused
[1mbad_code.py[m[36m:[m7[36m:[m1[36m:[m [1m[31mF401[m 'sys' imported but unused
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hflake8 bad_code.py[?2004l
[1mbad_code.py[m[36m:[m3[36m:[m80[36m:[m [1m[31mE501[m line too long (121 > 79 characters)
[1mbad_code.py[m[36m:[m6[36m:[m1[36m:[m [1m[31mF401[m 'os' imported but unused
[1mbad_code.py[m[36m:[m7[36m:[m1[36m:[m [1m[31mF401[m 'sys' imported but unused
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hflake8 bad_code.py[18Db[2Cck[P[12C [?2004l
[1mAll done! ✨ 🍰 ✨[0m
[34m1 file [0mleft unchanged.
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hblack bad_code.py[17Df[2Cke8 bad_code.py[?2004l
[1mbad_code.py[m[36m:[m3[36m:[m80[36m:[m [1m[31mE501[m line too long (121 > 79 characters)
[1mbad_code.py[m[36m:[m6[36m:[m1[36m:[m [1m[31mF401[m 'os' imported but unused
[1mbad_code.py[m[36m:[m7[36m:[m1[36m:[m [1m[31mF401[m 'sys' imported but unused
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hflake8 bad_code.py[18Db[2Cck[P[12C [?2004l
[1mreformatted bad_code.py[0m

[1mAll done! ✨ 🍰 ✨[0m
[34m[1m1 file [0m[1mreformatted[0m.
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hblack bad_code.py[17Df[2Cke8 bad_code.py[?2004l
[1mbad_code.py[m[36m:[m3[36m:[m80[36m:[m [1m[31mE501[m line too long (121 > 79 characters)
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[7mpip install vulture[27m[19D[27mp[27mi[27mp[27m [27mi[27mn[27ms[27mt[27ma[27ml[27ml[27m [27mv[27mu[27ml[27mt[27mu[27mr[27me[P[16C [17Dp[P[16C [17D[P[16C [17Dc install vulture[16Dco install vulture[16Dn install vulture[16Dd install vulture[16Da install vulture[16D[?2004l
Channels:
 - defaults
Platform: osx-arm64
Collecting package metadata (repodata.json): - \ | / done
Solving environment: \ failed

PackagesNotFoundError: The following packages are not available from current channels:

  - vulture

Current channels:

  - defaults
  - https://repo.anaconda.com/pkgs/main
  - https://repo.anaconda.com/pkgs/r

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.


[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hppip install vulture[?2004l

[1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m A new release of pip is available: [0m[31;49m24.3.1[0m[39;49m -> [0m[32;49m25.1[0m
[1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m To update, run: [0m[32;49mpython3.13 -m pip install --upgrade pip[0m
[1;31merror[0m: [1mexternally-managed-environment[0m

[31m×[0m This environment is externally managed
[31m╰─>[0m To install Python packages system-wide, try brew install
[31m   [0m xyz, where xyz is the package you are trying to
[31m   [0m install.
[31m   [0m 
[31m   [0m If you wish to install a Python library that isn't in Homebrew,
[31m   [0m use a virtual environment:
[31m   [0m 
[31m   [0m python3 -m venv path/to/venv
[31m   [0m source path/to/venv/bin/activate
[31m   [0m python3 -m pip install xyz
[31m   [0m 
[31m   [0m If you wish to install a Python application that isn't in Homebrew,
[31m   [0m it may be easiest to use 'pipx install xyz', which will manage a
[31m   [0m virtual environment for you. You can install pipx with
[31m   [0m 
[31m   [0m brew install pipx
[31m   [0m 
[31m   [0m You may restore the old behavior of pip by passing
[31m   [0m the '--break-system-packages' flag to pip, or by adding
[31m   [0m 'break-system-packages = true' to your pip.conf file. The latter
[31m   [0m will permanently disable this error.
[31m   [0m 
[31m   [0m If you disable this error, we STRONGLY recommend that you additionally
[31m   [0m pass the '--user' flag to pip, or set 'user = true' in your pip.conf
[31m   [0m file. Failure to do this can result in a broken Homebrew installation.
[31m   [0m 
[31m   [0m Read more about this behavior here: <https://peps.python.org/pep-0668/>

[1;35mnote[0m: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
[1;36mhint[0m: See PEP 668 for the detailed specification.
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[7mpip install vulture[27m[19D[27mp[27mi[27mp[27m [27mi[27mn[27ms[27mt[27ma[27ml[27ml[27m [27mv[27mu[27ml[27mt[27mu[27mr[27me[?2004l

[1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m A new release of pip is available: [0m[31;49m24.3.1[0m[39;49m -> [0m[32;49m25.1[0m
[1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m To update, run: [0m[32;49mpython3.13 -m pip install --upgrade pip[0m
[1;31merror[0m: [1mexternally-managed-environment[0m

[31m×[0m This environment is externally managed
[31m╰─>[0m To install Python packages system-wide, try brew install
[31m   [0m xyz, where xyz is the package you are trying to
[31m   [0m install.
[31m   [0m 
[31m   [0m If you wish to install a Python library that isn't in Homebrew,
[31m   [0m use a virtual environment:
[31m   [0m 
[31m   [0m python3 -m venv path/to/venv
[31m   [0m source path/to/venv/bin/activate
[31m   [0m python3 -m pip install xyz
[31m   [0m 
[31m   [0m If you wish to install a Python application that isn't in Homebrew,
[31m   [0m it may be easiest to use 'pipx install xyz', which will manage a
[31m   [0m virtual environment for you. You can install pipx with
[31m   [0m 
[31m   [0m brew install pipx
[31m   [0m 
[31m   [0m You may restore the old behavior of pip by passing
[31m   [0m the '--break-system-packages' flag to pip, or by adding
[31m   [0m 'break-system-packages = true' to your pip.conf file. The latter
[31m   [0m will permanently disable this error.
[31m   [0m 
[31m   [0m If you disable this error, we STRONGLY recommend that you additionally
[31m   [0m pass the '--user' flag to pip, or set 'user = true' in your pip.conf
[31m   [0m file. Failure to do this can result in a broken Homebrew installation.
[31m   [0m 
[31m   [0m Read more about this behavior here: <https://peps.python.org/pep-0668/>

[1;35mnote[0m: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
[1;36mhint[0m: See PEP 668 for the detailed specification.
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[H[2J[0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hlls[?2004l
bad_code.py		mle_setup.md		README.md		requirements.txt
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hggit push origin .[?2004l
fatal: invalid refspec '.'
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hgit push origin .       [?2004l
fatal: The current branch setup/python-tools has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin setup/python-tools

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.

[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[7mgit push --set-upstream origin setup/python-tools[27m[49D[27mg[27mi[27mt[27m [27mp[27mu[27ms[27mh[27m [27m-[27m-[27ms[27me[27mt[27m-[27mu[27mp[27ms[27mt[27mr[27me[27ma[27mm[27m [27mo[27mr[27mi[27mg[27mi[27mn[27m [27ms[27me[27mt[27mu[27mp[27m/[27mp[27my[27mt[27mh[27mo[27mn[27m-[27mt[27mo[27mo[27ml[27ms0s[1C  [?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hgit push [7morigin setup/python-tools[27m[25D[27mo[27mr[27mi[27mg[27mi[27mn[27m [27ms[27me[27mt[27mu[27mp[27m/[27mp[27my[27mt[27mh[27mo[27mn[27m-[27mt[27mo[27mo[27ml[27ms[?2004l
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'setup/python-tools' on GitHub by visiting:[K
remote:      https://github.com/s1tishlinux/python-mle-setup/pull/new/setup/python-tools[K
remote: 
To github.com:s1tishlinux/python-mle-setup.git
 * [new branch]      setup/python-tools -> setup/python-tools
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hggit status[?2004l
On branch setup/python-tools
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	[31m.pylintrc[m
	[31mbad_code.py[m
	[31mmle_setup.md[m
	[31mrequirements.txt[m

nothing added to commit but untracked files present (use "git add" to track)
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hggit add *[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[H[2J[0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [Kggit status[?2004l
On branch setup/python-tools
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	[32mnew file:   bad_code.py[m
	[32mnew file:   mle_setup.md[m
	[32mnew file:   requirements.txt[m

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	[31m.pylintrc[m

[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hgit statusadd * .  .*[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hgit add .*status[?2004l
On branch setup/python-tools
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	[32mnew file:   .pylintrc[m
	[32mnew file:   bad_code.py[m
	[32mnew file:   mle_setup.md[m
	[32mnew file:   requirements.txt[m

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	[31mmodified:   mle_setup.md[m

[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hgit statusadd .*  .[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hgit add .status[?2004l
On branch setup/python-tools
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	[32mnew file:   .pylintrc[m
	[32mnew file:   bad_code.py[m
	[32mnew file:   mle_setup.md[m
	[32mnew file:   requirements.txt[m

[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004h[H[2J[0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[H[2J[0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004l
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hlls[?2004l
bad_code.py		mle_setup.md		README.md		requirements.txt
[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hggit status[?2004l
On branch setup/python-tools
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	[32mnew file:   .pylintrc[m
	[32mnew file:   bad_code.py[m
	[32mnew file:   mle_setup.md[m
	[32mnew file:   requirements.txt[m

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	[31mmodified:   mle_setup.md[m

[1m[7m%[27m[1m[0m                                                                                                                                                                          [0m[27m[24m[J(mle-env) satishgundu@Satishs-MacBook-Air python-mle-setup % [K[?2004hgit status[10Dls        [8Dgit status       g  