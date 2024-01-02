#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Paul", "James")
say_my_name("Nhlobo", "Novice")
say_my_name("jac")
try:
    say_my_name(12, "Novice")
except Exception as e:
    print(e)
