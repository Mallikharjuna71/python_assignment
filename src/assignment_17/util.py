def arrange_blocks(l):
    if l == sorted(l):
        return 'Yes'
    l = l[::-1]
    if len(l)%2!=0:
        length = len(l)
        if l[length//2]>l[(length//2)-1] or l[length//2]>l[(length//2)+1]:
            return 'No'
    for i in range((len(l)//2)-1):
        j = (i*-1)-1
        if l[i]<l[i+1] or l[j]<l[j-1]:
            return 'No'
    return 'Yes'
