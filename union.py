n=int(input())
english_subs=set(map(int,input().split()))
b=int(input())
french_subs=set(map(int,input().split()))
total_sub=english_subs.intersection(french_subs)
print(len(total_sub))
                 
