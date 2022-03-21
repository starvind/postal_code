target = 81
best_m = 0
best_n = 0
best_q = 0
for m in range(1,target,1):
	for n in range(1,target,1):
		current_sum = m + n
		q = 0
		a = m 
		b = n  
		while current_sum <= target : 
			current_sum = a + b 
			q += 1
			if current_sum == target and q > best_q:
#				print(m,"\t",n,"\t",q)
				best_m = m 
				best_n = n 
				best_q = q 
			a = b 
			b = current_sum

print(best_m, best_n, best_q)
