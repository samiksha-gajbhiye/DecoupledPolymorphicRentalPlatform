import { useEffect, useRef, useState } from 'react';
import { CalendarDays } from 'lucide-react';

const toDisplayDate = (value) => {
  if (!value) return '';
  const [year, month, day] = value.split('-');
  return year && month && day ? `${day}/${month}/${year}` : value;
};

const toIsoDate = (value) => {
  const match = value.match(/^(\d{1,2})\/(\d{1,2})\/(\d{4})$/);
  if (!match) return value;

  const [, day, month, year] = match;
  return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`;
};

const getParts = (value) => {
  const displayValue = toDisplayDate(value);
  const [day = '', month = '', year = ''] = displayValue.split('/');
  return { day, month, year };
};

const DateInput = ({ value = '', onChange = () => {}, id, className = '', min, ...inputProps }) => {
  const [parts, setParts] = useState(getParts(value));
  const calendarRef = useRef(null);

  useEffect(() => {
    setParts(getParts(value));
  }, [value]);

  const emitChange = (nextParts, event) => {
    const nextDisplay = `${nextParts.day}/${nextParts.month}/${nextParts.year}`;
    const nextIso = toIsoDate(nextDisplay);
    onChange({ target: { ...event.target, value: nextIso } });
  };

  const handlePartChange = (part, event) => {
    const nextParts = { ...parts, [part]: event.target.value.replace(/\D/g, '').slice(0, part === 'year' ? 4 : 2) };
    setParts(nextParts);
    emitChange(nextParts, event);
  };

  const handleCalendarChange = (event) => {
    setParts(getParts(event.target.value));
    onChange(event);
  };

  return (
    <span className={`date-input ${className}`}>
      <input {...inputProps} type="text" id={id} value={parts.day} onChange={(event) => handlePartChange('day', event)} placeholder="dd" inputMode="numeric" maxLength={2} aria-label="Day" autoComplete="off" />
      <b>/</b>
      <input type="text" value={parts.month} onChange={(event) => handlePartChange('month', event)} placeholder="mm" inputMode="numeric" maxLength={2} aria-label="Month" autoComplete="off" />
      <b>/</b>
      <input type="text" value={parts.year} onChange={(event) => handlePartChange('year', event)} placeholder="yyyy" inputMode="numeric" maxLength={4} aria-label="Year" autoComplete="off" />
      <button type="button" className="date-calendar" aria-label="Choose date from calendar" onClick={() => calendarRef.current?.showPicker?.()}>
        <CalendarDays size={16} />
      </button>
      <input ref={calendarRef} id={`${id}-calendar`} className="date-calendar-native" type="date" value={value || ''} onChange={handleCalendarChange} min={min} tabIndex={-1} aria-hidden="true" />
    </span>
  );
};

export default DateInput;
