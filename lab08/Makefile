cc=gcc
EXE=foo
JAVAC=javac
JRE=java
PAGER=less
TEST_OUT=test.out
EXP_OUT=expected.out

.PHONY: clean run-py run-c read run-java save-java test-java

foo.o : foo.c foo.h
	$(cc) -c foo.c

main.o : main.c foo.h
	$(cc) -c main.c
	
$(EXE) : foo.o main.o
	$(cc) -o$(EXE) main.o foo.o

run-c : $(EXE)
	./$(EXE)

run-py : foo.py
	./foo.py

read : README
	$(PAGER) README

foo.class : foo.java
	$(JAVAC) foo

run-java : foo.class
	$(JRE) foo

save-java :
	$(JRE) foo > $(TEST_OUT)

test-java : 
	-@if diff $(TEST_OUT) $(EXP_OUT) &> /dev/null ; then \
	echo "Passed" ;\
	else \
		echo "Not the same!" ;\
		fi

clean : 
	rm test.out foo.class main.o foo.o $(EXE)
