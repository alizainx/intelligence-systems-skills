# Nontrivial Implementation & Multi-File Engineering Walkthrough: `vhdl-strong-typed-rtl`

- **Target File**: `examples/saturating_counter.vhdl`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity saturating_counter is
    generic (
        WIDTH : positive := 8
    );
    port (
        clk   : in  std_logic;
        rst_n : in  std_logic;
        en    : in  std_logic;
        count : out unsigned(WIDTH - 1 downto 0)
    );
end entity saturating_counter;

architecture rtl of saturating_counter is
    constant MAX_VAL : unsigned(WIDTH - 1 downto 0) := (others => '1');
    signal cnt_q     : unsigned(WIDTH - 1 downto 0) := (others => '0');
begin
    process(clk, rst_n) is
    begin
        if rst_n = '0' then
            cnt_q <= (others => '0');
        elsif rising_edge(clk) then
            if en = '1' and cnt_q < MAX_VAL then
                cnt_q <= cnt_q + 1;
            end if;
        end if;
    end process;
    count <= cnt_q;
end architecture rtl;

```
