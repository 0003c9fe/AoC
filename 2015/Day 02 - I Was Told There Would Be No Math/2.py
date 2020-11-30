with open('input.txt') as file:
    input = [line.rstrip() for line in file]

def dimensionsToPaper(dim):
    l, w, h = dim[0], dim[1], dim[2]
    return 2*(l*w + l*h + w*h) + min(l*w,l*h,w*h)

def dimensionsToRibbon(dim):
    l, w, h = dim[0], dim[1], dim[2]
    return min(2*(l+w),2*(l+h),2*(w+h)) + l*w*h

paperAmount = 0
ribbonAmount = 0
for present in input:
    dimensions = list(map(int,present.split('x')))
    paperAmount += dimensionsToPaper(dimensions)
    ribbonAmount += dimensionsToRibbon(dimensions)

print('The elves need to order',paperAmount,'square feet of wrapping paper')
print('The elves need to order',ribbonAmount,'feet of ribbon')
