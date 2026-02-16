import { Calculator } from "lucide-react";
import { Button } from "@heroui/react";

export function ButtonSearch({ onClick, loading }) {
  return (
    <div className="flex flex-wrap gap-3">
      <Button className="w-full" onClick={onClick} disabled={loading}>
        <Calculator />
        {loading ? "Simulando..." : "Simular Economia"}
      </Button>
    </div>
  );
}
