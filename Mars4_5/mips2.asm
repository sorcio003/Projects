.data

	array: .word 0,1,4,2,7,8,4,6
	dim: .word 8
	
.text

Main:
	addi $s0,$zero, 4		#i
	addi $t0,$zero, 32
	lw $s1, array($zero)	#x = array [0]
	
Loop:
	beq $s0, $t0, end	#while
	lw $t2, array($s0)	#array[i]
	slt $t1, $s1, $t2
	beq $t1, $zero, else
	addi $s1, $t2, 0	#x = array[i]
	else:
	addi $s0, $s0, 4	# i=i+1
	
	j Loop	
end:
	addi $a0, $s1, 0
	li $v0, 1
	syscall
	
	li $v0, 10
	syscall
	
	
	
	