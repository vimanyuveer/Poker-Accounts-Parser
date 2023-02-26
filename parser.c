#include <stdio.h>
#include <stdlib.h>

int main(){

	// Open the text file.
	FILE *rec_File;
	rec_File = fopen("/Users/vimanyu/Desktop/poker_records.txt", "r");
	if (rec_File == NULL){
		printf("ERROR! File path is invalid.");
		return -1;
	}

	// Get size in bytes of the file by moving to the end and using ftell and reset to initial position.
	fseek(rec_File, 0, SEEK_END);
	int size = ftell(rec_File);
	fseek(rec_File, 0, SEEK_SET);

	// Store the file into a sting dynamically.
	char *text;
	text = (char *) malloc(size);
	for (int i =0; ; i+=0){
		text[i] = fgetc(rec_File);
		if (text[i] == EOF)
			break;
	}

	// Interface and get names list from user.
/*
	printf("Size is %d", size);
	printf("Enter Names (NULL to stop) -->");
*/

	// // Read entire data into a string
	// for(int i = 0; text[i] != EOF; i ++){
	// 	fscanf(rec_File, "%c", &text[i]);
	// 	if(i == SIZE - 1){
	// 		printf("ERROR! String too large.");
	// 		return -1;
	// 	}
	// }



	fclose(rec_File);
	return 0;
}