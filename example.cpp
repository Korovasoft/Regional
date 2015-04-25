#include <iostream>
#include <vector>

// My main program
int main(int argc, char** argv) {
	std::vector dummy;
	// @region NiceLoop
	for(int i = 0; i < 10; i++) {
		std::cout << "Halp!" << std::endl;
	}
	// @endregion
	return 0;
}
