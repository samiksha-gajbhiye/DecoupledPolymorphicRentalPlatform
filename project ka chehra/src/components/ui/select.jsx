import * as React from "react";
import {
  Select as PrimitiveSelect,
  SelectContent as PrimitiveSelectContent,
  SelectItem as PrimitiveSelectItem,
  SelectTrigger as PrimitiveSelectTrigger,
  SelectValue as PrimitiveSelectValue,
} from "@radix-ui/react-select";

const Select = React.forwardRef(
  ({ className, children, ...props }, ref) => (
    <PrimitiveSelect
      ref={ref}
      className="select select-sm w-full bg-background border border-input hover:border-accent focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50"
      {...props}
    >
      {children}
    </PrimitiveSelect>
  )
);
Select.displayName = PrimitiveSelect.displayName;

const SelectTrigger = React.forwardRef(
  ({ className, children, ...props }, ref) => (
    <PrimitiveSelectTrigger
      ref={ref}
      className="select-trigger flex h-10 w-full items-center justify-between rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-transparent file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50[&>svg]:pointer-events-none[&>svg]:size-4[&>svg]:shrink-0"
      {...props}
    >
      {children}
    </PrimitiveSelectTrigger>
  )
);
SelectTrigger.displayName = PrimitiveSelectTrigger.displayName;

const SelectValue = React.forwardRef(
  ({ className, children, ...props }, ref) => (
    <PrimitiveSelectValue
      ref={ref}
      className="tracking-wipe"
      {...props}
    >
      {children}
    </PrimitiveSelectValue>
  )
);
SelectValue.displayName = PrimitiveSelectValue.displayName;

const SelectContent = React.forwardRef(
  ({ className, children, ...props }, ref) => (
    <PrimitiveSelectContent
      ref={ref}
      className="select-content z-50 min-h-[8rem] w-full max-h-96 overflow-hidden rounded-md border bg-popover p-1 text-sm shadow-md data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2"
      {...props}
    >
      {children}
    </PrimitiveSelectContent>
  )
);
SelectContent.displayName = PrimitiveSelectContent.displayName;

const SelectItem = React.forwardRef(
  ({ className, children, ...props }, ref) => (
    <PrimitiveSelectItem
      ref={ref}
      className="select-item flex h-10 w-full items-center justify-between rounded-lg border bg-transparent px-3 py-2 text-sm cursor-default outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-20"
      {...props}
    >
      {children}
    </PrimitiveSelectItem>
  )
);
SelectItem.displayName = PrimitiveSelectItem.displayName;

export {
  Select,
  SelectTrigger,
  SelectValue,
  SelectContent,
  SelectItem,
};