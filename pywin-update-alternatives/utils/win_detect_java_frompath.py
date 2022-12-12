import winreg, os

class win_detect_java_frompath:
    reg_path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
    reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)

@classmethod
def get_as_user_env():
    reg_path = r'USER\Environment'
    reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path)
    return reg_path, reg_key

@classmethod
def get_as_sys_env():
    reg_path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
    reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)
    return reg_path, reg_key

@classmethod
def get_detect():
    system_environment_variables = winreg.QueryValueEx(reg_key, 'Path')[0]
    system_environment_variables = system_environment_variables.split(";")

    # initializing substrings
    subs_java = 'java'
    subs_jre = 'jre'
    subs_jdk = 'jdk'
    
    # using list comprehension
    # to get string with substring
    java_detect_res = [i for i in system_environment_variables if subs_java.IGNORECASE in i]
    
    jdk_detect_res = [i for i in java_detect_res if subs_jre.IGNORECASE not in i]
    jre_detect_res = [i for i in java_detect_res if subs_jdk.IGNORECASE not in i]
        
    return (jdk_detect_res, jre_detect_res)

@classmethod
def get_current_version():
    def run_command(command):
        p = subprocess.Popen(command,
        stdout = subprocess.PIPE,
        stderr = subprocess.STDOUT)
        return iter(p.stdout.readline, b'')
    
    out = list(run_command("java -version"))
    return out