import queue

"""
FIND_SOLUTION:
    Define this function in BinPacking.py, along with any auxiliary
functions that you need.  Do not change the Driver.py file at all.
--------------------------------------------------
rectangles: a list of tuples, e.g. [(w1, l1), ... (wn, ln)] where
    w1 = width of rectangle 1,
    l1 = length of rectangle 1, etc.
--------------------------------------------------
RETURNS: a list of tuples that designate the top left corner placement,
         e.g. [(x1, y1), ... (xn, yn)] where
         x1 = top left x coordinate of rectangle 1 placement
         y1 = top left y coordinate of rectangle 1 placement, etc.
"""

locs = {}

def find_solution(rectangles):  
    rect_to_place = enqueue(rectangles)
    place(0,0,rect_to_place)
    packed_rects = reorder()
    
    return packed_rects  # a working example!

def reorder():
    rects = []

    for i in range(len(locs)):
        rects.append(locs[i])

    return rects

def enqueue(rectangles):
    rectqueue = []
    i = 0

    for rect in rectangles:
        w = rect[0]
        h = rect[1]
        rectqueue.append(Rectangle(i,w,h))
        i+=1

    rectqueue = sorted(rectqueue)
    return rectqueue

def place(curx, cury, rects):
    while len(rects) > 0:
        rect = rects.pop()
        space = []

        if rect.w > rect.h:
            locs[rect.id]= (0,cury)
            if rect.w > curx:
                space.append(Empty_Space(curx, 0, rect.w-curx, cury))
                curx=rect.w
            else:
                space.append(Empty_Space(rect.w, cury, curx-rect.w, rect.h))
            cury+=rect.h
        else:
            locs[rect.id]=(curx,0)
            if rect.h > cury:
                space.append(Empty_Space(0, cury, curx, rect.h-cury))
                cury=rect.h
            else:
                space.append(Empty_Space(curx, rect.h, rect.w, cury-rect.h))
            curx+=rect.w        

        space = sorted(space)
        ###fill_spaces(space,rects)
        #place(curx,cury,rects)

def fill_spaces(spaces, rects):
    
    print('here')


class Rectangle:
    def __init__(self,id , w,h):
        self.w = w
        self.h = h
        self.id = id
    
    def __lt__(self, other):
        if self.w > other.w and self.w > other.h and self.w > self.h:
            return self.w
        elif self.h > other.w and self.h > other.h and self.h > self.w:
            return self.h
        elif other.w > self.w and other.w > other.h and other.w > self.h:
            return other.w
        elif other.h > other.w and self.w < other.h and other.h > self.h:
            return other.h

class Empty_Space:
    def __init__(self,x,y, w, h):
        self.pt = (x,y)
        self.w = w
        self.h = h

    def __lt__(self, other):
        if self.w < other.w and self.w < other.h and self.w < self.h:
            return self.w
        elif self.h < other.w and self.h < other.h and self.h < self.w:
            return self.h
        elif other.w < self.w and other.w < other.h and other.w < self.h:
            return other.w
        elif other.h < other.w and self.w > other.h and other.h < self.h:
            return other.h
        
        
