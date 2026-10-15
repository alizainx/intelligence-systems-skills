`default_nettype none
module axis_skid_buffer #(
    parameter integer DATA_W = 32
) (
    input  wire              clk,
    input  wire              rst_n,
    input  wire              s_valid,
    output wire              s_ready,
    input  wire [DATA_W-1:0] s_data,
    output reg               m_valid,
    input  wire              m_ready,
    output reg  [DATA_W-1:0] m_data
);
    reg               skid_valid;
    reg  [DATA_W-1:0] skid_data;

    assign s_ready = !skid_valid;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            m_valid    <= 1'b0;
            m_data     <= {DATA_W{1'b0}};
            skid_valid <= 1'b0;
            skid_data  <= {DATA_W{1'b0}};
        end else begin
            if (skid_valid) begin
                if (m_ready) begin
                    m_data     <= skid_data;
                    skid_valid <= 1'b0;
                end
            end else if (s_valid) begin
                if (!m_valid || m_ready) begin
                    m_valid <= 1'b1;
                    m_data  <= s_data;
                end else begin
                    skid_valid <= 1'b1;
                    skid_data  <= s_data;
                end
            end else if (m_ready) begin
                m_valid <= 1'b0;
            end
        end
    end
endmodule
`default_nettype wire
