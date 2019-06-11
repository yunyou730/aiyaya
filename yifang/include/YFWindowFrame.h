#pragma once
#include <glfw3.h>

namespace yf
{
	class WindowFrame
	{
	public:
		WindowFrame();
		~WindowFrame();

		bool create();
		void mainloop();

	private:
		GLFWwindow*		_window = nullptr;
	};
}


