package main

import (
 "testing"
 "github.com/moov-io/iso8583"
 "github.com/moov-io/iso8583/specs"
)

func TestRoundTrip(t *testing.T) {
 mti, amount, err := RoundTrip()
 if err != nil { t.Fatal(err) }
 if mti != "0100" { t.Fatalf("mti inattendu: %s", mti) }
 if amount != "000000001000" { t.Fatalf("montant inattendu: %s", amount) }
}

// Une entrée invalide doit être rejetée par Unpack; aucun réseau n'est utilisé.
func TestTruncatedMessage(t *testing.T) {
 msg := iso8583.NewMessage(specs.Spec87ASCII)
 if err := msg.Unpack([]byte("0100")); err == nil {
  t.Fatal("le message tronqué ne doit pas être accepté")
 }
}

func TestUnsupportedField(t *testing.T) {
 msg := iso8583.NewMessage(specs.Spec87ASCII)
 if err := msg.Field(129, "1"); err == nil {
  t.Fatal("le champ hors du périmètre ISO 8583 pédagogique doit être rejeté")
 }
}
