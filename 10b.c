#include <stdio.h>

int main(int argc, char *argv[]) {
	FILE *fp;

	fp = fopen("./day10.txt", "r");
	
	char line[255]; 
	char letter;
	
	long medians[255];
	int index_m = 0;
	while (fgets(line, 255, fp)) {	
		int score = 0;
		char prev = '!';
		char indices[255];
		int index = 0;
		char corrupt = 'N';
		for (int i = 0; line[i] != 0; i++) {
			letter = line[i];
			prev = indices[index-1];
			switch (letter) {
				case '}':
					if (prev != '{') {
						corrupt = '{';
					}
					else {
						score = (score*5)+3;
						index -= 1;
					}	
					break;
				case '{':
					indices[index] = '{';
					index += 1;
					break;
				case '(':
					indices[index] = '(';
					index += 1;
					break;
				case ')':
					if (prev != '(') {
						corrupt = '(';
					}
					else {
						score = (score*5)+1;
						index -= 1;
					}
					break;
				case '[':
					indices[index] = '[';
					index += 1;
					break;
				case ']':
					if (prev != '[') {	
						corrupt = '[';
					}
					else {
						score = (score*5)+2;
						index -= 1;
					}
					break;
				case '<':
					indices[index] = '<';
					index += 1;
					break;
				case '>':
					if (prev != '<') {
						corrupt = '<';
					}
					else {
						score = (score*5)+4;
						index -= 1;
					}
					break;
			}
			if (corrupt != 'N') {
				indices[0] = '?';
				break;
			}
		}
		indices[index] = '\0';
		long score2 = 0;
		if (indices[0] != '?') {
			for (int i = 0; indices[i] != 0; i++) {
				switch (indices[(index-1)-i]) {
					case '<':
						score2 = (score2*5)+4;
						break;
					case '{':
						score2 = (score2*5)+3;
						break;
					case '[':
						score2 = (score2*5)+2;
						break;
					case '(':
						score2 = (score2*5)+1;
						break;
				}
			}
			medians[index_m] = score2;
			index_m += 1;
		}
	}
	medians[index_m] = 0;
	fclose(fp);
	int half = index_m/2;
	long bubble_sort[index_m];
	for (int i = 0; medians[i] != 0; i++) {
		int point = 0;
		for (int j = 0; medians[j] != 0; j++) {	
			if (j != i) {
				if (medians[i] > medians[j]) {
					point += 1;
				}
			}
		}
		printf("%i %ld\n", point, medians[i]);	
	}
	printf("Median: %i\n", half);
	return 0;
}
