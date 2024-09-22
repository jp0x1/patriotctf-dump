```C
int64_t shrimp()
{
    FILE* fp = fopen("/flag.txt", &data_402008);
    
    if (fp == 0)
        return puts("Flag file not found, contact an …");
    
    for (char i = fgetc(fp); i != 0xff; i = fgetc(fp))
        putchar(i);
    
    return fclose(fp);
}

int32_t main(int32_t argc, char** argv, char** envp)
{
    puts("Welcome to the shrimplest challe…");
    i = 0;
    
    while (i <= 2)
    {
        printf("Remember to just keep it shrimpl…");
        void buf;
        fgets(&buf, 0x32, stdin);
        puts("Adding shrimp...");
        int64_t var_48;
        __builtin_strncpy(&var_48, "so easy and so shrimple, have fun!", 0x23);
        strncat(&var_48, &buf, 0x32);
        printf("You shrimped the following: %s\n", &var_48);
        i += 1;
    }
    
    return puts("That's it, hope you did somethin…");
}

void __libc_csu_init()
{
    _init();
    int64_t i = 0;
    
    do
    {
        int64_t rdx;
        int64_t rsi;
        int32_t rdi;
        __frame_dummy_init_array_entry[i](rdi, rsi, rdx);
        i += 1;
    } while (2 != i);
}

void __libc_csu_fini() __pure
{
    return;
}

int64_t _fini() __pure
{
    return;
}
```