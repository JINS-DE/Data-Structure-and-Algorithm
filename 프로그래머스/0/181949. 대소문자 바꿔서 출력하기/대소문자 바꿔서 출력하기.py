str = input()
answer=''
for st in str:
    if st.isupper():
        answer+=st.lower()
    else:
        answer+=st.upper()
print(answer)
        