#!/usr/bin/env python3
import sys
import random

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def render(time, a, b, d, color1, color2, color3, v1, v2, v3, v4):
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(color1, color2, color3)
    glBegin(GL_TRIANGLES)
    glVertex2f(-a / 2 + v1, 0)
    glVertex2f(a / 2 + v2, 0)
    glVertex2f(a / 2 + v3, b)
    glEnd()

    glColor3f(color3, color2, color1)
    glBegin(GL_TRIANGLES)
    glVertex2f(-a / 2 + v1, 0.0)
    glVertex2f(-a / 2 + v4, b)
    glVertex2f(a / 2 + v3, b)
    glEnd()

    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    print("Define a:")
    a = int(input())
    print("Define b:")
    b = int(input())
    print("Define d:")
    d = float(input())

    v1 = random.uniform(0.0, d)
    v2 = random.uniform(0.0, d)
    v3 = random.uniform(0.0, d)
    v4 = random.uniform(0.0, d)

    color1 = random.random()
    color2 = random.random()
    color3 = random.random()

    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime(), a, b, d, color1, color2, color3, v1, v2, v3, v4)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
