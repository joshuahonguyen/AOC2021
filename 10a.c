#include <stdio.h>

int main(int argc, char *argv[]) {
	FILE *fp;

	fp = fopen("./day10.txt", "r");
	
	char line[255]; 
	char letter;
	
	int score = 0;
	while (fgets(line, 255, fp)) {	
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
						index -= 1;
					}
					break;
			}
			if (corrupt != 'N') {
				if (corrupt == '{') {
					score = score+1197;
				}
				else if (corrupt == '[') {
					score = score+57;
				}
				else if (corrupt == '(') {
					score = score+3;
				}
				else if (corrupt == '<') {
					score = score+25137;
				}
				break;
			}
		}
		indices[index] = '\0';
		printf("%s\n", indices);
		
	}
	printf("Score %i\n", score);
	fclose(fp);
	
	return 0;
}
