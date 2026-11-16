// OPB-D03-001 — Démonstration de messagerie ISO 8583, sans réseau ni données de carte.
// This is a local-only educational example, not a payment switch or card authorization.
package main

import (
 "fmt"
 "github.com/moov-io/iso8583"
 "github.com/moov-io/iso8583/specs"
)

// RoundTrip encode un message fictif puis le décode localement.
// MTI 0100 signifie ici seulement un type de message d'exercice.
// Les champs 3, 4 et 11 sont tous synthétiques; aucun PAN ou PIN.
func RoundTrip() (string, string, error) {
 msg := iso8583.NewMessage(specs.Spec87ASCII)
 if err := msg.MTI("0100"); err != nil { return "", "", fmt.Errorf("mti: %w", err) }
 for _, f := range []struct{ id int; value string }{
  {3, "000000"}, // Code de traitement fictif (6 chiffres)
  {4, "000000001000"}, // Montant fictif : 12 chiffres, unité définie par la spec pédagogique
  {11, "000001"}, // Numéro de suivi fictif (STAN)
 } {
  if err := msg.Field(f.id, f.value); err != nil { return "", "", fmt.Errorf("field %d: %w", f.id, err) }
 }
 payload, err := msg.Pack()
 if err != nil { return "", "", fmt.Errorf("pack: %w", err) }
 // Ne jamais imprimer de messages ISO 8583 bruts dans un système réel : des champs sensibles peuvent y figurer.
 received := iso8583.NewMessage(specs.Spec87ASCII)
 if err := received.Unpack(payload); err != nil { return "", "", fmt.Errorf("unpack: %w", err) }
 mti, err := received.GetMTI()
 if err != nil { return "", "", fmt.Errorf("get mti: %w", err) }
 amount, err := received.GetString(4)
 if err != nil { return "", "", fmt.Errorf("get amount: %w", err) }
 return mti, amount, nil
}

func main() {
 mti, amount, err := RoundTrip()
 if err != nil { panic(err) }
 fmt.Printf("Message fictif décodé : MTI=%s, champ 4=%s (aucun paiement exécuté)\n", mti, amount)
}
