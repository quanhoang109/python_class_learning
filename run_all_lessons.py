#!/usr/bin/env python3
"""
Run all OOP lessons in sequence
"""

import os
import sys

lessons = [
    "lessons/01_classes_and_objects.py",
    "lessons/02_attributes_and_methods.py",
    "lessons/03_encapsulation.py",
    "lessons/04_inheritance.py",
]

def run_lessons():
    print("="*70)
    print("PYTHON OOP TUTORIAL - RUNNING ALL LESSONS")
    print("="*70)

    for i, lesson in enumerate(lessons, 1):
        if not os.path.exists(lesson):
            print(f"\n⚠️  Lesson {i} not found: {lesson}")
            continue

        print(f"\n\n{'#'*70}")
        print(f"# RUNNING LESSON {i}: {lesson}")
        print(f"{'#'*70}\n")

        try:
            with open(lesson) as f:
                code = f.read()
                exec(code)
        except Exception as e:
            print(f"\n❌ Error running {lesson}: {e}")
            continue

        input(f"\n\nPress Enter to continue to next lesson...")

    print("\n\n" + "="*70)
    print("ALL LESSONS COMPLETED!")
    print("="*70)
    print("\nNext steps:")
    print("1. Review EXERCISES.md")
    print("2. Complete practice exercises")
    print("3. Build your own projects")
    print("\nHappy coding! 🚀\n")

if __name__ == "__main__":
    run_lessons()
