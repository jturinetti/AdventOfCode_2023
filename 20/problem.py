import time
import logging
from my_utils import read_aoc_data

def flip_flop(current: int):
    return int(not bool(current))
    
def conjunction(d: dict, linked: list, memory: dict):
    # # TESTING
    # for x in linked:
    #     logging.debug('      cur val of {}: {}'.format(x, memory[x]))
    # # *******
    
    output = int(not all(bool(memory[l]) for l in linked))
    logging.debug('      outputting {} to next instruction'.format(output))
    return output

def parse_input(input):
    d = {}
    c_list = []
    for i in input:
        si = i.split(' -> ')
        key = si[0]
        subdict = {
            'type': key[0] if key[0] in ('%', '&') else key,
            'targets': si[1].split(', '),
            'val': 0
        }
        if key != 'broadcaster':
            key = key[1:]
        if subdict['type'] == '&':
            c_list.append(key)
        d[key] = subdict
    
    # map conjuction nodes to linked modules
    for c in c_list:
        linked = []
        for k in d.keys():
            if c in d[k]['targets']:
                linked.append(k)
        d[c]['linked'] = linked
        d[c]['memory'] = {}
        for x in linked:
            d[c]['memory'][x] = 0
    logging.debug(d)
    return d

# count_dict = {}

def pulse_tostr(val: int):
    if val == 0:
        return 'low'
    if val == 1:
        return 'high'

def process(d: dict, q: list, new_q: list):
    # instruction structure: (prev_key, target_key, pulse (0 or 1))
    high = low = 0
    while (len(q) > 0):
        targets = []
        ins = q.pop(0)
        key = ins[1]
        next_pulse = ins[2]

        if next_pulse == 0:
            low += 1
        elif next_pulse == 1:
            high += 1

        logging.debug ('    processing {}: {} -{}-> {}'.format(key, ins[0], pulse_tostr(next_pulse), key))        

        if not key in d:
            continue
        
        t = d[key]
        if t['type'] == '%':
            if next_pulse == 0:
                logging.debug('     type: %')
                next_pulse = flip_flop(t['val'])
                t['val'] = next_pulse
                targets += t['targets']
            else:
                logging.debug('     do nothing')     
        elif t['type'] == '&':
            logging.debug('     type: &')
            t['memory'][ins[0]] = next_pulse
            next_pulse = conjunction(d, t['linked'], t['memory'])
            t['val'] = next_pulse
            targets += t['targets']
        else:
            targets += t['targets']
        
        for x in targets:
            logging.debug((key, x, next_pulse))
            new_q.append((key, x, next_pulse))
    return (d, q, new_q, high, low)

def press_button(num_presses, d: dict):
    total_high = total_low = 0
    for x in range(num_presses):
        cycle_high = cycle_low = 0
        logging.debug('CYCLE {}'.format(x + 1))
        qq = []
        cur_q = [('button', 'broadcaster', 0)]

        while len(cur_q) > 0 or len(qq) > 0:
            if len(cur_q) == 0:
                cur_q = qq.pop(0)
                continue
            
            (d, cur_q, next_q, high, low) = process(d, cur_q, [])
            logging.debug('    high and low pulse counts for last instruction: {}, {}'.format(high, low))
            cycle_high += high
            cycle_low += low
            qq.append(next_q)

        logging.debug('   CYCLE {} high and low pulse counts: {}, {}'.format(x + 1, cycle_high, cycle_low))
        total_high += cycle_high
        total_low += cycle_low

    logging.debug('total high: {}, total low: {}'.format(total_high, total_low))
    return (total_high, total_low)

# solution functions
def part_a(input):
    d = parse_input(input)
    logging.debug(d)
    (total_high, total_low) = press_button(1000, d)
    return total_high * total_low

def part_b(input):
    # TODO
    return

def execute():
    input_data = read_aoc_data(20, 2023)    # replace with correct day and year
    start_time = time.perf_counter()
    logging.info('part_a answer: {}'.format(part_a(input_data)))
    end_time = time.perf_counter()
    logging.info(f"part_a perf: {(end_time - start_time):02f}s")
    start_time = time.perf_counter()
    logging.info('part_b answer: {}'.format(part_b(input_data)))
    end_time = time.perf_counter()
    logging.info(f"part_b perf: {(end_time - start_time):02f}s")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    execute()