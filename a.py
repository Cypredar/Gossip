system = System()

system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain() # clock

system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')] # memory

system.cpu = TimingSimpleCPU() # cpu

system.membus = SystemXBar()

system.cpu.icache_port = system.membus.cpu_side_ports # port
system.cpu.dcache_port = system.membus.cpu_side_ports
system.cpu.icache_port = system.l1_cache.cpu_side
system.cpu.icache_port = system.membus.cpu_side_ports
system.cpu.createInterruptController()
system.system_port = system.membus.cpu_side_ports
system.mem_ctrl = MemCtrl()

system.workload = SEWorkload.init_compatible(binary) # os

binary = 'tests/test-progs/hello/bin/x86/linux/hello' # executable
process = Process()
process.cmd = [binary]
system.cpu.workload = process
system.cpu.createThreads()

root = Root(full_system = False, system = system)
m5.instantiate()

exit_event = m5.simulate() # start simulation
