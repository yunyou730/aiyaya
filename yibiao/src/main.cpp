#include <iostream>
#include <YFEngine.h>

using namespace yf;

int main()
{
	freopen("d:/test1.txt","w",stdout);
	freopen("d:/test1.txt", "w", stderr);

	yf::WindowFrame frame;
	frame.create();
	frame.mainloop();
	return 0;
}
