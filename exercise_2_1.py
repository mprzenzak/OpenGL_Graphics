import math
import random

import numpy as np
from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLUT import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0, 0, 0, 1.0)
    glEnable(GL_DEPTH_TEST)


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
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio,
                10.0, -10.0)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5,
                10.0, -10.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def axes():
    x_min = (-5.0, 0.0, 0.0)
    x_max = (5.0, 0.0, 0.0)

    y_min = (0.0, -5.0, 0.0)
    y_max = (0.0, 5.0, 0.0)

    z_min = (0.0, 0.0, -5.0)
    z_max = (0.0, 0.0, 5.0)

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex3fv(x_min)
    glVertex3fv(x_max)
    glEnd()

    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)

    glVertex3fv(y_min)
    glVertex3fv(y_max)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)

    glVertex3fv(z_min)
    glVertex3fv(z_max)
    glEnd()


def egg(size):
    vertices_list = np.zeros((size, size, 3))
    for i in range(size):
        for j in range(size):
            u = i / (size - 1)
            v = j / (size - 1)
            vertices_list[i][j][0] = (-90.0 * pow(u, 5.0) + 225.0 * pow(u, 4.0) - 270.0 *
                                      pow(u, 3.0) + 180.0 * pow(u, 2.0) - 45.0 * u) * math.cos(math.pi * v)
            vertices_list[i][j][1] = 160.0 * pow(u, 4.0) - 320.0 * pow(u, 3.0) + 160.0 * pow(u, 2.0) - 5
            vertices_list[i][j][2] = (-90.0 * pow(u, 5.0) + 225.0 * pow(u, 4.0) - 270.0 * pow(u, 3.0) + 180.0 *
                                      pow(u, 2.0) - 45.0 * u) * math.sin(math.pi * v)
    # draw_points(vertices_list, size)
    # draw_lines(vertices_list, size)
    draw_triangles(vertices_list, generate_colors(size), size)


def draw_points(vertices_tab, size):
    glColor3f(1.0, 1.0, 1.0)

    glBegin(GL_POINTS)
    for i in range(size):
        for j in range(size):
            glVertex3fv(vertices_tab[i][j])
    glEnd()


def draw_lines(t, n):
    glColor3f(0.0, 1.0, 0.0)
    for w in range(1, n):
        for k in range(n - 1):
            lines_per_node(t, w, k)


def lines_per_node(vertices_list, x, y):
    glBegin(GL_LINES)

    glVertex3fv(vertices_list[x][y])
    glVertex3fv(vertices_list[x - 1][y])

    glEnd()

    glBegin(GL_LINES)

    glVertex3fv(vertices_list[x][y])
    glVertex3fv(vertices_list[x][y + 1])

    glEnd()

    glBegin(GL_LINES)

    glVertex3fv(vertices_list[x][y])
    glVertex3fv(vertices_list[x - 1][y + 1])

    glEnd()


def draw_triangles(nodes, colors, n):
    for w in range(n):
        for k in range(n - 1):
            triangles_per_node(nodes, colors, w, k)


def triangles_per_node(nodes, colors, w, k):
    glBegin(GL_TRIANGLES)

    glColor3f(colors[w][k][0], colors[w][k][1], colors[w][k][2])
    glVertex3fv(nodes[w][k])
    glColor3f(colors[w - 1][k][0], colors[w - 1][k][1], colors[w - 1][k][2])
    glVertex3fv(nodes[w - 1][k])
    glColor3f(colors[w - 1][k + 1][0], colors[w - 1][k + 1][1], colors[w - 1][k + 1][2])
    glVertex3fv(nodes[w - 1][k + 1])

    glEnd()

    glBegin(GL_TRIANGLES)

    glColor3f(colors[w][k][0], colors[w][k][1], colors[w][k][2])
    glVertex3fv(nodes[w][k])
    glColor3f(colors[w][k + 1][0], colors[w][k + 1][1], colors[w][k + 1][2])
    glVertex3fv(nodes[w][k + 1])
    glColor3f(colors[w - 1][k + 1][0], colors[w - 1][k + 1][1], colors[w - 1][k + 1][2])
    glVertex3fv(nodes[w - 1][k + 1])

    glEnd()


def generate_colors(n):
    tab = np.zeros((n, n, 3))
    for i in range(n):
        for j in range(n):
            tab[i][j] = random.random()
    return tab


def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)


def render(size):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    axes()

    spin(glfwGetTime() * 180 / 3.1415)

    egg(size)

    glFlush()


def main():
    print("Define egg size:")
    size = int(input())

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
        render(size)
        glfwSwapBuffers(window)
        glfwPollEvents()

    glfwTerminate()


if __name__ == '__main__':
    main()
