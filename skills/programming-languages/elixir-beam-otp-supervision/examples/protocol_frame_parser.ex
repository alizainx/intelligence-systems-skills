defmodule Iss.Elixir.ProtocolFrameParser do
  @moduledoc "Safe binary protocol parser with sub-binary copy isolation."

  @spec parse_frame(binary()) :: {:ok, %{version: non_neg_integer(), payload: binary()}} | {:error, atom()}
  def parse_frame(<<0xA5, version::unsigned-integer-size(8), len::unsigned-big-integer-size(16), rest::binary>>) do
    if byte_size(rest) == len do
      {:ok, %{version: version, payload: :binary.copy(rest)}}
    else
      {:error, :length_mismatch}
    end
  end
  def parse_frame(_other), do: {:error, :invalid_header}
end
