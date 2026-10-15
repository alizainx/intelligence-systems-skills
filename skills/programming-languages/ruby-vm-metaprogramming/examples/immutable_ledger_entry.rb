# frozen_string_literal: true

LedgerCommand = Data.define(:account_id, :amount_cents) do
  def initialize(account_id:, amount_cents:)
    raise ArgumentError, "account_id must be Integer" unless account_id.is_a?(Integer) && account_id.positive?
    raise ArgumentError, "amount_cents must be Integer" unless amount_cents.is_a?(Integer)
    super(account_id: account_id, amount_cents: amount_cents)
  end
end
