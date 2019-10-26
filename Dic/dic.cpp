#include <iostream>
#include <cstdio>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <unistd.h>
#include <cstring>
#define MAX_BUFFER_SIZE 8192

using namespace std;

int main(int argc, char* argv[]) {
    string s;
    string inputStr; 
    pid_t pid;
    int exit_code;

    /* build input*/
    const string str1 = "-b";
    string str2 = argv[1];
    if (argc == 2 && !str1.compare(str2)) {
        /* buffer method*/
        while (cin >> s) {
            inputStr += s;
            inputStr += " ";
        }
    } else {
        /* sys var*/
        string tempStr = "";
        string tmp = "";
        for (int i = 1; i < argc; i++) {
            s = argv[i];
            inputStr += s;
            inputStr += " ";
        }
    }
        
    
    if (inputStr.length() >= MAX_BUFFER_SIZE) {
        cout << ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" << endl;
        cout << "WARRNING: Too much input, has been cut!" << endl;
        cout << "警告:输入内容过多, 已截断!" << endl;
        cout << ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" << endl;
    }

    pid = fork();

    /* buffer guard*/
    char buffer[MAX_BUFFER_SIZE];
    strcpy(buffer, inputStr.c_str());
    char queryStr[MAX_BUFFER_SIZE];
    snprintf(queryStr, sizeof(queryStr), "%s", buffer);
    
    switch (pid) {
        case -1:
            perror("fork failed");
            exit(1);
            break;
            
        case 0: {
            exit_code = 37;
            char* execv_str[] = {"dic", queryStr, NULL};
            if (execv("/bin/dic", execv_str) < 0) {
                perror("error on exec");
                exit(0);
            }
            break;
        }

        default:
            exit_code = 0;
            break;
    }

    if (pid != 0) {
        int stat_val;
        pid_t child_pid;

        child_pid = wait(&stat_val);
        //cout << "stat_val = " << stat_val << endl;
        if (WIFEXITED(stat_val)) {
            //cout << "child exited with the code " << WEXITSTATUS(stat_val) << endl;
        } else {
            cout << "child terminated abnormally" << endl;
        }
        exit(exit_code);
    }
    exit(0);
}

