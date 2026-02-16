import { Calculator } from "lucide-react";
import { Button } from "@heroui/react";

export function ButtonSearch() {
  return (
    <div className="flex flex-wrap gap-3">
      <Button className="w-full">
        <Calculator />
        Calcular Economia
      </Button>
    </div>
  );
}
