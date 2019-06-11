#include "YFWindowFrame.h"
#include <iostream>

using namespace yf;

WindowFrame::WindowFrame()
{
	glfwInit();
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
	glfwWindowHint(GLFW_RESIZABLE, GL_FALSE);
}

WindowFrame::~WindowFrame()
{
	glfwTerminate();
}

bool WindowFrame::create()
{
	_window = glfwCreateWindow(800, 600, "LearnOpenGL", nullptr, nullptr);
	if (_window == nullptr)
	{
		std::cout << "Failed to create GLFW window" << std::endl;
		glfwTerminate();
		return false;
	}
	glfwMakeContextCurrent(_window);
	return true;
}

void WindowFrame::mainloop()
{
	if (_window == nullptr)
	{
		return;
	}
	while (!glfwWindowShouldClose(_window))
	{
		glfwPollEvents();
		glfwSwapBuffers(_window);
	}
}
