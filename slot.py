import numpy as np
import pandas as pd
import datetime


class Setting():
    def __init__(self):
        self.screen_size = [3,3,3,3,3]
        
        self.strip_input_b = [
[2,2,2,3,3,3,4,4,4,5,5,5,10,8,8,6,10,7,7,10,8,10,6,9,6,10,10,7,8,8,5,5,4,5,4,3,3,3,5,3,5,4,3,5,4,8,10,6,6,10,6,10,8,8,7,10,9,9,7,10,7,10,9,8,9,8,7,9,9,7,7,7,6,7,9,6,10,7,9,9,7,6,9,6,6,9,8,6,8,2,6,8,9,2,10,6,7,2,9,8],
[0,0,0,0,0,0,0,0,0,0,7,10,10,6,9,9,10,7,10,8,7,10,8,7,7,8,8,10,3,5,4,3,4,0,5,4,5,5,4,5,4,5,0,3,4,3,5,3,5,3,5,3,4,3,4,4,3,5,5,5,4,5,4,3,4,5,5,4,8,6,9,9,6,7,10,10,10,6,7,6,9,6,10,8,7,2,10,6,9,2,9,10,8,2,6,10,8,2,10,6,1,8,8,1,9,6,1,7,6,1,2,8,1,9,9,1,9,8,1,9,2,1,9,8,1,8,8,1,6,8,2,6,9,7,2,9,7,10,2,7,6,7,2,9,6,7,10,7,8,9],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,9,10,8,7,6,6,10,4,3,4,4,5,0,3,4,4,5,3,3,4,3,0,4,5,4,5,4,3,5,4,5,5,3,5,3,4,5,3,5,4,5,4,4,5,4,5,5,4,3,5,8,9,9,10,9,7,9,7,10,8,9,9,10,8,2,7,6,8,2,10,8,7,2,10,10,9,2,7,7,1,6,8,1,10,7,1,9,7,1,8,7,1,6,6,1,10,7,1,8,6,1,6,8,1,9,6,1,7,10,2,6,10,8,2,7,6,9,2,6,10,7,2,9,8,9,7,8,9,6],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,6,7,8,10,6,6,7,10,7,10,6,7,7,5,4,4,3,4,0,3,4,5,4,5,5,4,5,0,4,3,5,4,3,3,4,5,5,4,5,4,3,5,3,5,4,4,3,3,5,3,5,6,8,8,10,9,10,8,6,8,8,10,7,9,6,6,9,8,9,6,2,10,9,10,2,9,8,8,2,8,6,9,2,10,7,1,10,7,1,2,6,1,8,10,1,10,9,1,2,8,1,7,6,1,9,10,1,6,2,1,6,10,1,8,9,2,8,9,9,2,9,8,6,2,9,9,6,2,10,7,6,9,8,7,7],
[2,2,2,3,3,3,4,4,4,5,5,5,9,10,10,7,6,7,8,10,9,8,9,8,7,9,6,6,7,6,5,3,5,5,3,4,4,3,5,5,4,4,5,3,5,6,10,7,10,10,9,7,9,10,6,9,10,7,9,9,8,6,8,8,9,7,8,7,7,8,7,6,7,6,9,9,6,7,10,6,7,8,10,8,8,2,10,8,6,2,10,10,10,2,6,6,8,2,9,8]
]
        self.strip_input_f = [
[2,2,2,4,4,4,3,3,3,5,5,5,9,8,7,8,6,9,10,7,7,10,7,10,7,7,8,9,9,6,6,9,8,8,8,6,9,10,7,6,9,7,9,10,7,10,6,10,6,6,3,5,4,5,4,4,5,4,5,3,3,5,4,5,5,3,10,10,6,9,8,6,9,7,10,9,6,7,6,8,10,8,8,9,8,6,7,8,2,10,10,6,2,7,8,9,2,8,7,9],
[0,0,0,0,0,0,0,0,0,0,9,10,7,10,10,8,10,8,7,9,10,10,9,7,10,8,6,8,9,8,10,9,10,8,7,10,9,8,10,7,9,9,10,8,9,10,10,7,10,10,5,5,3,4,0,2,5,4,4,3,5,4,5,3,5,3,2,4,5,5,4,3,5,3,4,4,2,3,3,4,2,4,3,0,5,3,4,5,2,4,0,5,4,5,10,10,8,7,10,10,8,10,7,9,0,10,9,8,0,9,10,7,0,6,10,7,2,9,7,8,2,10,9,10,2,9,10,9,2,7,10,10,2,10,8,1,6,10,1,10,8,1,8,10,1,10,7,1,7,9],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,8,10,9,10,8,10,10,10,7,10,7,10,8,9,7,8,8,7,8,9,7,6,8,9,7,7,3,4,3,3,2,4,3,2,4,4,5,4,3,4,4,5,0,4,3,5,5,2,5,4,5,5,4,2,5,0,3,5,5,3,4,3,5,3,2,5,0,4,4,5,7,10,10,7,6,9,0,10,9,7,0,9,10,7,0,10,10,9,0,10,6,8,2,8,10,8,2,9,8,8,2,10,6,9,2,10,8,10,2,10,6,1,7,8,1,8,6,1,9,7,1,9,10,1,7,9],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,8,9,10,9,8,9,7,6,9,4,2,5,5,3,5,0,2,5,4,5,5,4,5,3,5,4,5,4,3,0,4,3,5,3,5,3,4,3,4,3,2,3,5,0,4,3,4,4,2,4,4,2,5,9,8,7,8,9,7,8,7,10,7,0,9,7,6,0,8,6,9,0,8,10,7,2,7,9,8,2,8,9,8,2,10,9,10,2,8,9,8,2,7,9,1,7,7,1,9,7,1,8,7,1,10,9,1,8,9],
[2,2,2,5,5,5,3,3,3,4,4,4,7,7,8,9,8,7,7,8,10,9,7,8,6,8,8,9,8,6,10,6,10,6,9,10,6,7,10,8,10,9,9,9,7,9,7,7,10,9,5,4,3,3,3,5,4,5,3,5,4,5,3,4,5,5,6,10,9,10,6,9,9,8,8,6,7,8,6,8,6,8,9,6,10,9,10,6,10,7,6,7,2,7,7,6,2,8,8,10]
]
        
        self.strip_b = strip_ring(self.screen_size, self.strip_input_b)
        self.strip_f = strip_ring(self.screen_size, self.strip_input_f)
        
        self.line_path = [[(0,1),(1,1),(2,1),(3,1),(4,1)],
                          [(0,0),(1,0),(2,0),(3,0),(4,0)],
                          [(0,2),(1,2),(2,2),(3,2),(4,2)],
                          [(0,0),(1,1),(2,2),(3,1),(4,0)],
                          [(0,2),(1,1),(2,0),(3,1),(4,2)],
                          [(0,0),(1,0),(2,1),(3,2),(4,2)],
                          [(0,2),(1,2),(2,1),(3,0),(4,0)],
                          [(0,1),(1,0),(2,1),(3,2),(4,1)],
                          [(0,1),(1,2),(2,1),(3,0),(4,1)],
                          [(0,0),(1,1),(2,1),(3,1),(4,0)],
                          [(0,2),(1,1),(2,1),(3,1),(4,2)],
                          [(0,1),(1,0),(2,0),(3,1),(4,2)],
                          [(0,1),(1,2),(2,2),(3,1),(4,0)],
                          [(0,1),(1,1),(2,0),(3,1),(4,2)],
                          [(0,1),(1,1),(2,2),(3,1),(4,0)],
                          [(0,0),(1,0),(2,1),(3,2),(4,1)],
                          [(0,2),(1,2),(2,1),(3,0),(4,1)],
                          [(0,1),(1,0),(2,1),(3,2),(4,2)],
                          [(0,1),(1,2),(2,1),(3,0),(4,0)],
                          [(0,0),(1,0),(2,0),(3,1),(4,2)]]
        
        self.pay_line = [{'ICON':[2,0], 'PAY':{3:20, 4:50, 5:500}},
                         {'ICON':[3,0], 'PAY':{3:20, 4:40, 5:300}},
                         {'ICON':[4,0], 'PAY':{3:15, 4:40, 5:200}},
                         {'ICON':[5,0], 'PAY':{3:10, 4:30, 5:150}},
                         {'ICON':[6,0], 'PAY':{3:5, 4:15, 5:50}},
                         {'ICON':[7,0], 'PAY':{3:5, 4:15, 5:50}},
                         {'ICON':[8,0], 'PAY':{3:5, 4:15, 5:50}},
                         {'ICON':[9,0], 'PAY':{3:5, 4:15, 5:50}},
                         {'ICON':[10,0], 'PAY':{3:5, 4:15, 5:50}}]
        
        self.pay_scatter = [{'ICON':[1], 'PAY':{3:60}}]
        
        self.pay_f_times = [{'ICON':[1], 'PAY':{3:8}}]
        
        self.pay_f_retrigger = [{'ICON':[1], 'PAY':{3:50}}]


        
        
def strip_ring(screen_size, strip_input):
    strip = []
    for i in range(len(strip_input)):
        s_add = strip_input[i] + strip_input[i][:screen_size[i] - 1]
        strip.append(s_add)
        
    return strip


def rand_strip(screen_size, strip):
    rnd = []
    screen = []
    for i in range(len(screen_size)):
        ri = np.random.randint(len(strip[i]) - screen_size[i] + 1)
        s_add = strip[i][ri:ri + screen_size[i]]
        rnd.append(ri)
        screen.append(s_add)
    
    screen = np.array(pd.DataFrame(screen))
    return screen
        

def score_line(screen, line_path, pay):
    score = 0
    for path in line_path:
        s_add = 0
        for p_dic in pay:
            combo = 0
            for xy in path:
                if screen[xy] in p_dic['ICON']:
                    combo += 1
                else:
                    break
                
            if combo in p_dic['PAY'].keys():
                s_add = max(s_add, p_dic['PAY'][combo])
            
        score += s_add
    
    return score
                
    
def score_way(screen, pay):
    score = 0
    for p_dic in pay:
        combo = 0
        lines = 1
        for i in range(len(screen)):
            l_prod = 0
            for icon in p_dic['ICON']:
                l_prod += np.count_nonzero(screen[i] == icon)
            
            if l_prod != 0:
                combo += 1
                lines *= l_prod
            else:
                break
            
        if combo in p_dic['PAY'].keys():
            score += p_dic['PAY'][combo] * lines
            
    return score


def score_scatter(screen, pay):
    score = 0
    for p_dic in pay:
        combo = 0
        
        if np.count_nonzero(screen == p_dic['ICON'][0]) == 0:
            continue
        
        for icon in p_dic['ICON']:
            combo += np.count_nonzero(screen == icon)
        
        if combo in p_dic['PAY'].keys():
            score += p_dic['PAY'][combo]
            
    return score


def screen_rotate(screen, degree):
    k = degree / 90    
    screen_copy = screen.copy()
    
    screen_part = np.rot90(screen_copy[1:4], k)
    screen_copy[1:4] = screen_part
    
    return screen_copy



        

def bg_play(game = Setting()):
    screen = rand_strip(game.screen_size, game.strip_b)
    
    score = score_line(screen, game.line_path, game.pay_line) + score_scatter(screen, game.pay_scatter)
    
    fg_times = score_scatter(screen, game.pay_f_times)
    
    bg_play.score = score
    bg_play.fg_times = fg_times
    
    
def fg_play(times, wild, game = Setting()):
    fs_times = times
    score = 0
    
    while fs_times != 0:
        screen_0 = rand_strip(game.screen_size, game.strip_f)
        score += score_line(screen_0, game.line_path, game.pay_line) + score_scatter(screen_0, game.pay_scatter)
        
        fs_add = score_scatter(screen_0, game.pay_f_retrigger)
        
        check_rot = 0
        for i in range(1, 4):
            if np.count_nonzero(screen_0[i] == wild) == 3:
                check_rot = 1
                break
        
        if check_rot == 1:
            screen_90 = screen_rotate(screen_0, 90)
            screen_180 = screen_rotate(screen_0, 180)
            screen_270 = screen_rotate(screen_0, 270)
            
            score += score_line(screen_90, game.line_path, game.pay_line) \
                    + score_line(screen_180, game.line_path, game.pay_line) \
                    + score_line(screen_270, game.line_path, game.pay_line)

        
        fs_times += fs_add - 1
        
    fg_play.score = score



bg_s = []
fg_s = []
s = []
N = 10000000
bet = 20
for i in range(N):
    if i % int(N/10) == 1:
        print(i, ' ---- ', np.mean(s))
        
    score = 0
    
    bg_play()
    score += bg_play.score / 20
    
    fg_play(bg_play.fg_times, 0)
    score += fg_play.score / 20
    
    bg_s.append(bg_play.score / 20)
    if fg_play.score != 0:
        fg_s.append(fg_play.score / 20)
    s.append(score)

bins = [-1,0,5,10,20,50,100,300,1000,5000,1000000]
s_cut = pd.cut(s,bins)
print("full game distribution:")
print(pd.value_counts(s_cut).sort_index())
print("full game RTP: ", np.mean(s))
print("bonus rate: ", len(fg_s)/N)
print("volatility: ", np.std(s, ddof = 1))
print("-----")
print("base game distribution:")
print(pd.value_counts(pd.cut(bg_s,bins), normalize = True).sort_index())
print("base game RTP: ", np.mean(bg_s))
print("-----")
print("bonus distribution:")
print(pd.value_counts(pd.cut(fg_s,bins), normalize = True).sort_index())
print("bonus RTP: ", np.mean(fg_s))
print("-----")




