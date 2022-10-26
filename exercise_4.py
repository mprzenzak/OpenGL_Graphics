#!/usr/bin/env python3
import sys
import random

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def startup():
    #update_viewport(400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def render(size, level, deformation):
    glClear(GL_COLOR_BUFFER_BIT)

    carpet(-size // 2, -size // 2, size, level, deformation)
    glFlush()


def draw(x, y, size, deformation):
    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 50.0)
    glVertex2f(50.0, 0.0)
    glEnd()
    # if deformation > 0:
    #     glBegin(GL_POLYGON)
    #
    #     glColor3f(random.random(), random.random(), random.random())
    #     glVertex2f(x + random.uniform(0.0, deformation) - deformation / 2,
    #                y + random.uniform(0.0, deformation) - deformation / 2)
    #     glColor3f(random.random(), random.random(), random.random())
    #     glVertex2f(x + random.uniform(0.0, deformation) - deformation / 2,
    #                y + size + random.uniform(0.0, deformation) - deformation / 2)
    #     glColor3f(random.random(), random.random(), random.random())
    #     glVertex2f(x + size + random.uniform(0.0, deformation) - deformation / 2,
    #                y + size + random.uniform(0.0, deformation) - deformation / 2)
    #     glColor3f(random.random(), random.random(), random.random())
    #     glVertex2f(x + size + random.uniform(0.0, deformation) - deformation / 2,
    #                y + random.uniform(0.0, deformation) - deformation / 2)
    #
    #     glEnd()
    #
    #
    # else:
    #     glBegin(GL_POLYGON)
    #
    #     glColor3f(random.random(), random.random(), random.random())
    #     glVertex2f(x, y)
    #     glColor3f(random.random(), random.random(), random.random())
    #     glVertex2f(x, y + size)
    #     glColor3f(random.random(), random.random(), random.random())
    #     glVertex2f(x + size, y + size)
    #     glColor3f(random.random(), random.random(), random.random())
    #     glVertex2f(x + size, y)
    #
    #     glEnd()


def carpet(x, y, size, level, deformation):
    size //= 3

    for w in range(x + 3 * size):
        for h in range(y + 3 * size):
            if (h - y) != size or (w - x) != size:
                if level != 0:
                    carpet(w, h, size, level - 1, deformation)
                else:
                    draw(w, h, size, deformation)
            h += size
        w += size


def update_viewport(width, height):
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
    print("Define edge length:")
    size = int(input())
    print("Define number of divisions:")
    level = int(input())
    print("Define deformation level:")
    deformation = float(input())

    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    # glutInitDisplayMode(GLUT_SINGLE)
    # glutReshapeFunc(update_viewport)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(size, level, deformation)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
